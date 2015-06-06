# -*- coding: utf-8 -*-


class Team(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Round(object):
    def __init__(self, id, type, round_data=None, prev_round=None, next_round=None):
        self.round_data = round_data if round_data is not None else {}
        self.id = id
        self.type = type
        self.prev_round = prev_round
        self.next_round = next_round


class RoundType(object):
    def __init__(self, id, type):
        self.id = id
        self.type = type


class RunningRound(object):
    def __init__(self, round):
        self.round = round
        self.running = False


def create_knock_out_phase(team_data, fields):
    round_data = {}
    count = 0
    for key in team_data['row1'].keys():
        round_data[count] = {'field': fields[count], 'teams': [{'name': team_data['row1'][key], 'result': 0},
                                                               {'name': team_data['row2'][key], 'result': 0}]}
        count += 1
    print(round_data)


def process_battle_results(round_data):
    pass