# -*- coding: utf-8 -*-
from kubb_match.data.models import Game, Round, KOPosition


class KnockOutService(object):
    def __init__(self):
        pass

    def create_initial_rounds(self, final_battle_positions):
        a_games = []
        a_positions = []
        b_games = []
        b_positions = []
        c_games = []
        c_positions = []
        d_games = []
        d_positions = []
        nr = int(len(final_battle_positions) / 5)
        for x in range(1, nr + 1, 1):
            team1 = next((pos for pos in final_battle_positions if pos.position == 'A' + str(x)))
            team2 = next((pos for pos in final_battle_positions if pos.position == 'B' + str(x)))
            game = Game(team1_id=team1.team_id, team2_id=team2.team_id)
            a_games.append(game)
            position1 = KOPosition(team_id=team1.team_id, position=16, same_position=16)
            position2 = KOPosition(team_id=team2.team_id, position=16, same_position=16)
            a_positions.append(position1)
            a_positions.append(position2)
        for x in range(1, nr + 1, 2):
            team1 = next((pos for pos in final_battle_positions if pos.position == 'C' + str(x)))
            team2 = next((pos for pos in final_battle_positions if pos.position == 'C' + str(x + 1)))
            game = Game(team1_id=team1.team_id, team2_id=team2.team_id)
            b_games.append(game)
            position1 = KOPosition(team_id=team1.team_id, position=24, same_position=8)
            position2 = KOPosition(team_id=team2.team_id, position=24, same_position=8)
            b_positions.append(position1)
            b_positions.append(position2)
        for x in range(1, nr + 1, 2):
            team1 = next((pos for pos in final_battle_positions if pos.position == 'D' + str(x)))
            team2 = next((pos for pos in final_battle_positions if pos.position == 'D' + str(x + 1)))
            game = Game(team1_id=team1.team_id, team2_id=team2.team_id)
            c_games.append(game)
            position1 = KOPosition(team_id=team1.team_id, position=32, same_position=8)
            position2 = KOPosition(team_id=team2.team_id, position=32, same_position=8)
            c_positions.append(position1)
            c_positions.append(position2)
        for x in range(1, nr + 1, 2):
            team1 = next((pos for pos in final_battle_positions if pos.position == 'E' + str(x)))
            team2 = next((pos for pos in final_battle_positions if pos.position == 'E' + str(x + 1)))
            game = Game(team1_id=team1.team_id, team2_id=team2.team_id)
            d_games.append(game)
            position1 = KOPosition(team_id=team1.team_id, position=40, same_position=8)
            position2 = KOPosition(team_id=team2.team_id, position=40, same_position=8)
            d_positions.append(position1)
            d_positions.append(position2)
        a_round = Round()
        a_round.games = a_games
        a_round.positions = a_positions
        b_round = Round()
        b_round.games = b_games
        b_round.positions = b_positions
        c_round = Round()
        c_round.games = c_games
        c_round.positions = c_positions
        d_round = Round()
        d_round.games = d_games
        d_round.positions = d_positions
        return {'A': a_round, 'B': b_round, 'C': c_round, 'D': d_round}

    def calculate_next_round(self, round):
        positions = self.calculate_positions(round)
        new_round = Round()
        new_round.positions = positions
        if positions[0].same_position > 1:
            new_round.games = self.create_games(positions)
            new_round.final = False
        else:
            new_round.final = True
        return new_round

    def calculate_positions(self, round):
        positions = []
        for game in round.games:
            t1_pos = next((pos for pos in round.positions if pos.team_id == game.team1_id))
            same_position = int(t1_pos.same_position / 2)
            win_pos = t1_pos.position - same_position
            los_pos = t1_pos.position
            if game.winner == game.team1_id:
                position1 = KOPosition(team_id=game.team1_id, position=win_pos, same_position=same_position)
                position2 = KOPosition(team_id=game.team2_id, position=los_pos, same_position=same_position)
            else:
                position1 = KOPosition(team_id=game.team2_id, position=win_pos, same_position=same_position)
                position2 = KOPosition(team_id=game.team1_id, position=los_pos, same_position=same_position)
            positions.append(position1)
            positions.append(position2)
        return positions

    def create_games(self, positions):
        games = []
        same_position_map = {}
        for pos in positions:
            if pos.position in same_position_map:
                same_position_map[pos.position].append(pos)
            else:
                same_position_map[pos.position] = [pos]
        for pos_key in same_position_map:
            for x in range(0, len(same_position_map[pos_key]), 2):
                team1 = same_position_map[pos_key][x]
                team2 = same_position_map[pos_key][x + 1]
                game = Game(team1_id=team1.team_id, team2_id=team2.team_id)
                games.append(game)
        return games
