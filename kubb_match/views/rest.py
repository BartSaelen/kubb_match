# -*- coding: utf-8 -*-
from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_defaults, view_config
from kubb_match.data.mappers import map_team, map_game
from kubb_match.data.models import Team
from kubb_match.service.tournament_service import TournamentService


class RestView(object):
    def __init__(self, request):
        self.request = request
        self.data_manager = request.data_managers['data_manager']

    def _get_json_body(self):
        try:
            json_body = self.request.json_body
        except AttributeError as e:
            raise HTTPBadRequest(detail="Request bevat geen json body. \n%s" % e)
        except ValueError as e:
            raise HTTPBadRequest(detail="Request bevat incorrecte json body. \n%s" % e)
        if 'id' in self.request.matchdict and 'id' not in json_body:
            json_body['id'] = self.request.matchdict['id']
        return json_body


@view_defaults(renderer='json', accept='application/json')
class TeamView(RestView):
    @view_config(route_name='teams',
                 request_method='GET',
                 permission='view',
                 renderer='listjson')
    def get_teams(self):
        return self.data_manager.get_teams()

    @view_config(route_name='team',
                 request_method='GET',
                 permission='view',
                 renderer='itemjson')
    def get_team(self):
        tid = self.request.matchdict['id']
        t = self.data_manager.get_team(tid)
        if not t:
            return HTTPNotFound()
        return t

    def edit_team(self, t, json_body):
        t = map_team(json_body, t)
        t = self.data_manager.save(t)
        return t

    @view_config(
        route_name='teams',
        request_method='POST',
        permission='admin',
        renderer='itemjson'
    )
    def add_team(self):
        team_data = self._get_json_body()
        t = Team()
        t = self.edit_team(t, team_data)
        self.request.response.status = '201'
        self.request.response.location = \
            self.request.route_path('team', id=t.id)
        return t

    @view_config(
        route_name='team',
        request_method='PUT',
        permission='admin',
        renderer='itemjson'
    )
    def update_team(self):
        tid = self.request.matchdict.get('id')
        t = self.data_manager.get_team(tid)
        if not t:
            return HTTPNotFound()
        team_data = self._get_json_body()
        if 'id' in self.request.matchdict and 'id' not in team_data:
            team_data['id'] = self.request.matchdict['id']
        t = self.edit_team(t, team_data)
        self.request.response.status = '200'
        self.request.response.location = \
            self.request.route_path('team', id=t.id)
        return t


@view_defaults(renderer='json', accept='application/json')
class RoundView(RestView):
    @view_config(route_name='rounds',
                 request_method='GET',
                 permission='view',
                 renderer='listjson')
    def get_rounds(self):
        return self.data_manager.get_rounds()

    @view_config(route_name='round',
                 request_method='GET',
                 permission='view',
                 renderer='itemjson')
    def get_round(self):
        rid = self.request.matchdict['id']
        r = self.data_manager.get_round(rid)
        if not r:
            return HTTPNotFound()
        return r

    @view_config(route_name='round_games',
                 request_method='GET',
                 permission='view',
                 renderer='listjson')
    def get_games(self):
        rid = self.request.matchdict['id']
        r = self.data_manager.get_round(rid)
        return r.games

    @view_config(route_name='round_game',
                 request_method='GET',
                 permission='view',
                 renderer='itemjson')
    def get_game(self):
        rid = self.request.matchdict['id']
        r = self.data_manager.get_round(rid)
        if not r:
            return HTTPNotFound()
        gid = self.request.matchdict['gid']
        game = self.data_manager.get_game(gid)
        return game

    @view_config(route_name='round_game',
                 request_method='PUT',
                 permission='view',
                 renderer='itemjson')
    def edit_game(self):
        rid = self.request.matchdict['id']
        r = self.data_manager.get_round(rid)
        if not r:
            return HTTPNotFound()
        gid = self.request.matchdict['gid']
        game = self.data_manager.get_game(gid)
        game_data = self._get_json_body()
        if 'gid' in self.request.matchdict and 'gid' not in game_data:
            game_data['gid'] = self.request.matchdict['gid']
        game = map_game(game_data, game)
        game = self.data_manager.save(game)
        return game

    @view_config(route_name='round_positions',
                 request_method='GET',
                 permission='view',
                 renderer='listjson')
    def get_positions(self):
        rid = self.request.matchdict['id']
        r = self.data_manager.get_round(rid)
        return r.positions


@view_defaults(renderer='json', accept='application/json')
class TournamentPhaseView(RestView):
    def __init__(self, request):
        super().__init__(request)
        self.tournament_service = TournamentService(self.data_manager)

    @view_config(route_name='phases',
                 request_method='GET',
                 permission='view',
                 renderer='listjson')
    def get_phases(self):
        return self.data_manager.get_phases()

    @view_config(route_name='phase',
                 request_method='GET',
                 permission='view',
                 renderer='itemjson')
    def get_phase(self):
        pid = self.request.matchdict['id']
        p = self.data_manager.get_phase(pid)
        if not p:
            return HTTPNotFound()
        return p

    @view_config(route_name='phase_status',
                 request_method='POST',
                 permission='view',
                 renderer='itemjson')
    def tournament_phase_status(self):
        data = self._get_json_body()
        pid = self.request.matchdict['id']
        if 'status' not in data:
            return HTTPBadRequest('status should be present')
        else:
            status = data['status']
        round = None
        p = self.data_manager.get_phase(pid)
        if status == 'init':
            if not p:
                return HTTPNotFound()
            if p.type == 'battle':
                round = self.tournament_service.init_battle_phase(p)
            elif p.type == 'ko':
                p1 = self.data_manager.get_phase(1)
                lr = next((r for r in p1.rounds if not r.played))
                round = self.tournament_service.init_ko_phase(p, lr.positions)
                round = round['A']
        elif status == 'next':
            if p.type == 'battle':
                round = self.tournament_service.next_battle_round(p)
            elif p.type == 'ko':
                round = self.tournament_service.next_ko_round(p)
                round = round[0]
        elif status == 'final':
            if p.type == 'battle':
                round = self.tournament_service.final_battle_round(p)
            elif p.type == 'ko':
                round = self.tournament_service.final_ko_round(p)
                round = round[0]
        else:
            return HTTPBadRequest('invalid phase_type')
        self.request.response.status = '201'
        self.request.response.location = \
            self.request.route_path('round', id=round.id)
