# -*- coding: utf-8 -*-
from kubb_match.data.models import Team, Round, Phase, Game


class DataManager(object):

    def __init__(self, session):
        '''

        :param session: a db session
        '''
        self.session = session

    def save(self, object):
        '''
        bewaar een bepaald advies

        :param advies: het te bewaren advies
        :return: het bewaarde advies
        '''
        self.session.add(object)
        self.session.flush()
        return object

    def get_teams(self):
        return self.session.query(Team).all()

    def get_team(self, team_id):
        return self.session.query(Team).get(team_id)

    def get_rounds(self):
        return self.session.query(Round).all()

    def get_round(self, round_id):
        return self.session.query(Round).get(round_id)

    def get_game(self, game_id):
        return self.session.query(Game).get(game_id)

    def get_phases(self):
        return self.session.query(Phase).all()

    def get_phase(self, phase_id):
        return self.session.query(Phase).get(phase_id)
