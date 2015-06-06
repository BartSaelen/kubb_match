# -*- coding: utf-8 -*-


class GameDataManager(object):

    def __init__(self):
        self.teams = {}

    def get(self, id):
        return self.teams[id]