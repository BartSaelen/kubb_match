# -*- coding: utf-8 -*-
from kubb_match.data.models import Team


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
