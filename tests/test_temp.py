# -*- coding: utf-8 -*-
import unittest
from kubb_match.data.data_managers import GameDataManager
from kubb_match.data.models import Phase, Team, Round, GridPosition
from kubb_match.service.battle_service import BattleService
from kubb_match.utils import print_round, print_round_results, grid_printer


class TempTests(unittest.TestCase):
    def setUp(self):
        self.data_manager = GameDataManager()
        self.battle_service = BattleService()

    def test(self):
        phase = Phase()
        phase.name = "battle"

        round1 = Round()

        positions = {}
        t = 1
        for row in ('A', 'B', 'C', 'D', 'E'):
            for x in range(1, 9):
                key = row + str(x)
                name = 'team {0}'.format(t)
                team = Team(id=t, name=name)
                grid_pos = GridPosition(position=key, team_id=team.id)
                grid_pos.team = team
                self.data_manager.teams[t] = team
                t += 1
                positions[key] = grid_pos

        round1.positions = positions

        grid_printer(positions)

        print()
        print()

        round1.games = self.battle_service.create_games(positions)

        print_round(round1)

        x = 1
        for game in round1.games:
            if x % 4 == 0:
                game.winner = game.team1_id
            elif x % 2 == 0:
                game.winner = game.team2_id
            else:
                game.winner = game.team1_id
            x += 1

        print()
        print()
        print_round_results(round1)

        print()
        print()
        print()
        print()

        round2 = self.battle_service.calculate_next_round(round1)

        print('--- round 2 ---')

        grid_printer(round2.positions)

        print()
        print()

        print_round(round2)

        x = 1
        for game in round2.games:
            if x % 4 == 0:
                game.winner = game.team1_id
            elif x % 2 == 0:
                game.winner = game.team2_id
            else:
                game.winner = game.team2_id
            x += 1

        print()
        print()
        print_round_results(round2)

        print()
        print()
        print()
        print()

        round3 = self.battle_service.calculate_next_round(round2)

        print('--- round 3 ---')

        grid_printer(round3.positions)

        print()
        print()

        print_round(round3)

        x = 1
        for game in round3.games:
            if x % 4 == 0:
                game.winner = game.team2_id
            elif x % 2 == 0:
                game.winner = game.team1_id
            else:
                game.winner = game.team2_id
            x += 1

        print()
        print()
        print_round_results(round3)

        round4 = self.battle_service.calculate_next_round(round3)

        print('--- round 4 ---')

        grid_printer(round4.positions)

        print()
        print()

        print_round(round4)

        x = 1
        for game in round4.games:
            if x % 4 == 0:
                game.winner = game.team2_id
            elif x % 2 == 0:
                game.winner = game.team1_id
            else:
                game.winner = game.team2_id
            x += 1

        print()
        print()
        print_round_results(round4)

        round5 = self.battle_service.calculate_next_round(round4)

        print('--- round 5 ---')

        grid_printer(round5.positions)

        print()
        print()

        print_round(round5)

        x = 1
        for game in round5.games:
            if x % 4 == 0:
                game.winner = game.team1_id
            elif x % 2 == 0:
                game.winner = game.team1_id
            else:
                game.winner = game.team2_id
            x += 1

        print()
        print()
        print_round_results(round5)

        print()
        print()
        print('--- final results battle ---')

        final_positions = self.battle_service.calculate_positions(round5)

        grid_printer(final_positions)
