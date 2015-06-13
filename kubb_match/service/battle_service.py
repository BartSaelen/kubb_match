# -*- coding: utf-8 -*-
from kubb_match.data.models import GridPosition, Round, Game


class BattleService(object):
    def __init__(self):
        pass

    def create_games(self, positions):
        games = []
        nr = int(len(positions) / 5)
        field = 1
        for row in ('A', 'B', 'C', 'D', 'E'):
            for x in range(1, nr + 1, 2):
                print(row + str(x))
                print(row + str(x + 1))
                team1 = next((pos for pos in positions if pos.position == row + str(x)))
                team2 = next((pos for pos in positions if pos.position == row + str(x + 1)))
                game = Game(team1_id=team1.team_id, team2_id=team2.team_id, field=field)
                games.append(game)
                field += 1
        return games

    def calculate_next_round(self, round, final=False):
        positions = self.calculate_positions(round)
        new_round = Round()
        new_round.positions = positions
        if not final:
            new_round.games = self.create_games(positions)
        return new_round

    def calculate_positions(self, round):
        positions = []
        losers = []
        for game in round.games:
            if game.winner == game.team1_id:
                grid_pos = self.position_winner(round, positions, game.team1_id, True)
                positions.append(grid_pos)
                losers.append(game.team2_id)
            else:
                grid_pos = self.position_winner(round, positions, game.team2_id, False)
                positions.append(grid_pos)
                losers.append(game.team1_id)
        for loser_id in losers:
            grid_pos = self.position_loser(round, positions, loser_id)
            positions.append(grid_pos)
        return positions

    def position_winner(self, round, positions, winner_id, pos_1):
        pos = next((pos for pos in round.positions if pos.team_id == winner_id))
        key = pos.position
        if key[0] == 'A':
            key = key
            row = key[0]
        else:
            row = self.move_row_up(key[0])
            pos = int(key[1])
            key = row + str(pos)
            #if key in [pos.position for pos in positions]:
            #    pos = pos + 1 if pos_1 else pos - 1
            #    key = row + str(pos)
        pos = int(key[1])
        while key in [pos.position for pos in positions]:
            pos += 1
            if pos > 8:
                pos -= 8
            key = row + str(pos)
        grid_pos = GridPosition(position=key, team_id=winner_id)
        return grid_pos

    def position_loser(self, round, positions, loser_id):
        pos = next((pos for pos in round.positions if pos.team_id == loser_id))
        key = pos.position
        if key[0] == 'E':
            row = 'E'
            pos = int(key[1])
            while key in [pos.position for pos in positions]:
                pos += 1
                if pos > 8:
                    pos -= 8
                key = row + str(pos)
        else:
            row = self.move_row_down(key[0])
            pos = int(key[1]) + 2
            if pos > 8:
                pos -= 8
            key = row + str(pos)
            while key in [pos.position for pos in positions]:
                pos += 1
                if pos > 8:
                    pos -= 8
                key = row + str(pos)
        grid_pos = GridPosition(position=key, team_id=loser_id)
        return grid_pos

    @staticmethod
    def move_row_up(row):
        return chr(ord(row) - 1)

    @staticmethod
    def move_row_down(row):
        return chr(ord(row) + 1)
