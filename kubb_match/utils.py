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


def create_games(positions):
    games = []
    nr = int(len(positions) / 5)
    for row in ('A', 'B', 'C', 'D', 'E'):
        for x in range(1, nr + 1, 2):
            team1 = positions[row + str(x)]
            team2 = positions[row + str(x + 1)]
            game = Game(team1_id=team1.team_id, team2_id=team2.team_id)
            games.append(game)
    return games


def calculate_next_round(round):
    positions = {}
    losers = []
    for game in round.games:
        if game.winner == game.team1_id:
            grid_pos = position_winner(round, positions, game.team1_id, True)
            positions[grid_pos.position] = grid_pos
            losers.append(game.team2_id)
        else:
            grid_pos = position_winner(round, positions, game.team2_id, False)
            positions[grid_pos.position] = grid_pos
            losers.append(game.team1_id)
    for loser_id in losers:
        grid_pos = position_loser(round, positions, loser_id)
        positions[grid_pos.position] = grid_pos
    new_round = Round()
    new_round.positions = positions
    new_round.games = create_games(positions)
    return new_round


def position_winner(round, positions, winner_id, pos_1):
    key = next((pos for pos in round.positions if round.positions[pos].team_id == winner_id))
    if key[0] == 'A':
        key = key
    else:
        row = move_row_up(key[0])
        pos = int(key[1])
        key = row + str(pos)
        if key in positions:
            pos = pos + 1 if pos_1 else pos - 1
            key = row + str(pos)
    grid_pos = GridPosition(position=key, team_id=winner_id)
    return grid_pos


def position_loser(round, positions, loser_id):
    key = next((pos for pos in round.positions if round.positions[pos].team_id == loser_id))
    if key[0] == 'E':
        row = 'E'
        pos = int(key[1])
        while key in positions:
            pos += 1
            if pos > 8:
                pos -= 8
            key = row + str(pos)
    else:
        row = move_row_down(key[0])
        pos = int(key[1]) + 2
        if pos > 8:
            pos -= 8
        key = row + str(pos)
        while key in positions:
            pos += 1
            if pos > 8:
                pos -= 8
            key = row + str(pos)
    grid_pos = GridPosition(position=key, team_id=loser_id)
    return grid_pos


def move_row_up(row):
    return chr(ord(row) - 1)


def move_row_down(row):
    return chr(ord(row) + 1)
