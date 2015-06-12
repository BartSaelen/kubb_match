# -*- coding: utf-8 -*-



def map_team(team_json, team):
    team.name = team_json.get('name', None)
    return team


def map_game(game_json, game):
    game.winner = game_json.get('winner', None)
    return game
