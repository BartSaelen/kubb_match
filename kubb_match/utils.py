# -*- coding: utf-8 -*-
from kubb_match.data.models import Game, GridPosition, Round


def grid_printer(positions):
    nr = int(len(positions) / 5)
    print('-' * nr * 5)
    for row in ('A', 'B', 'C', 'D', 'E'):
        row_string = row + ' | '
        for x in range(1, nr + 1):
            key = row + str(x)
            row_string = row_string + str(positions[key].team_id) + ' | '
        print(row_string)
    print('-' * nr * 5)


def print_round(round):
    for game in round.games:
        print(str(game.team1_id) + ' - ' + str(game.team2_id))


def print_round_results(round):
    for game in round.games:
        print(str(game.team1_id) + ' - ' + str(game.team2_id) + ' | ' + str(game.winner))

