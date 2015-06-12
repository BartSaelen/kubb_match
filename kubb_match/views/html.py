# -*- coding: utf-8 -*-
from pyramid.view import view_defaults, view_config


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

    # ADMIN

    @view_config(route_name='phase1-admin', renderer='phase1-admin.jinja2', permission='admin')
    def admin(self):
        p = self.data_manager.get_phase(1)
        if len(p.rounds) > 0:
            current_round = next((r for r in p.rounds if not r.played))
            current_games = current_round.games
            current_games.sort(key=lambda x: x.field, reverse=False)
        else:
            current_games = None
            current_round = None
        return {'current_games': current_games, 'current_round': current_round}
