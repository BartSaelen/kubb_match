# -*- coding: utf-8 -*-


def grid_printer(positions):
    nr = int(len(positions) / 5)
    print('-' * nr * 5)
    for row in ('A', 'B', 'C', 'D', 'E'):
        row_string = row + ' | '
        for x in range(1, nr + 1):
            key = row + str(x)
            pos = next((pos for pos in positions if pos.position == key))
            row_string = row_string + str(pos.team_id) + ' | '
        print(row_string)
    print('-' * nr * 5)


def ko_position_printer(positions):
    print('-' * 15)
    for pos in positions:
        print(pos.team_id, pos.position)
    print('-' * 15)


def print_round(round):
    if hasattr(round, 'games'):
        for game in round.games:
            print(str(game.team1_id) + ' - ' + str(game.team2_id))


def print_round_results(round):
    if hasattr(round, 'games'):
        for game in round.games:
            print(str(game.team1_id) + ' - ' + str(game.team2_id) + ' | ' + str(game.winner))
