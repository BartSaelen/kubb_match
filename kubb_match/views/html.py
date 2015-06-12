# -*- coding: utf-8 -*-
import collections
from pyramid.view import view_defaults, view_config
from kubb_match.data.models import Round


@view_defaults(request_method='GET', accept='text/html')
class HtmlView(object):
    def __init__(self, request):
        self.request = request
        self.data_manager = request.data_managers['data_manager']

    @view_config(route_name='home', renderer='home.jinja2')
    def home(self):

        return {}

    @view_config(route_name='phase1', renderer='phase1.jinja2')
    def phase1(self):
        p = self.data_manager.get_phase(1)
        if len(p.rounds) > 0:
            current_round = next((r for r in p.rounds if not r.played))
            current_games = current_round.games
            current_games.sort(key=lambda x: x.field, reverse=False)
            position_data = {}
            for position in current_round.positions:
                position_data[position.position] = position
        else:
            current_games = None
            position_data = None
        return {'current_games': current_games, 'position_data': position_data}

    @view_config(route_name='phase2', renderer='phase2.jinja2')
    def phase2(self):
        p = self.data_manager.get_phase(2)
        if len(p.rounds) > 0:
            ko_rounds = [r for r in p.rounds if not r.played]
            current_games ={}
            position_data ={}
            for r in ko_rounds:
                games = r.games
                games.sort(key=lambda x: x.field, reverse=False)
                current_games[r.label] = games
                positions = {}
                r.positions.sort(key=lambda x: x.position, reverse=False)
                for pos in r.positions:
                    if pos.position in positions:
                        positions[pos.position].append(pos)
                    else:
                        positions[pos.position] = [pos]
                position_data[r.label] = collections.OrderedDict(sorted(positions.items()))
        else:
            current_games = None
            position_data = None
        return {'current_games': current_games, 'position_data': position_data}

    # ADMIN

    @view_config(route_name='phase1-admin', renderer='phase1-admin.jinja2', permission='admin')
    def admin1(self):
        p = self.data_manager.get_phase(1)
        if len(p.rounds) > 0:
            current_round = next((r for r in p.rounds if not r.played))
            current_games = current_round.games
            current_games.sort(key=lambda x: x.field, reverse=False)
        else:
            current_games = None
            current_round = None
        return {'current_games': current_games, 'current_round': current_round}

    @view_config(route_name='phase2-admin', renderer='phase2-admin.jinja2', permission='admin')
    def admin2(self):
        p = self.data_manager.get_phase(2)
        if len(p.rounds) > 0:
            ko_rounds = [r for r in p.rounds if not r.played]
            current_games ={}
            current_round ={}
            for r in ko_rounds:
                games = r.games
                games.sort(key=lambda x: x.field, reverse=False)
                current_games[r.label] = games
                current_round[r.label] = r.id
        else:
            current_games = None
            current_round = None
        return {'current_games': current_games, 'current_round': current_round}

    @view_config(route_name='results', renderer='results.jinja2')
    def results(self):
        p = self.data_manager.get_phase(2)
        if len(p.rounds) > 0:
            ko_rounds = [r for r in p.rounds if r.final]
            position_data ={}
            for r in ko_rounds:
                positions = {}
                for pos in r.positions:
                    if pos.position in positions:
                        positions[pos.position].append(pos)
                    else:
                        positions[pos.position] = [pos]
                position_data[r.label] = positions
        else:
            position_data = None
        return {'position_data': position_data}