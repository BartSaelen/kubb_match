# -*- coding: utf-8 -*-


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
        object = self.session.add(object)
        self.session.flush()
        return object