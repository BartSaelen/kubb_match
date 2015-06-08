# -*- coding: utf-8 -*-
from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_defaults, view_config
from kubb_match.data.mappers import map_team
from kubb_match.data.models import Team


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
    def get_advies(self):
        tid = self.request.matchdict['id']
        a = self.data_manager.get_team(tid)
        if not a:
            return HTTPNotFound()
        return a

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
        t = self.data_manager.get(tid)
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

