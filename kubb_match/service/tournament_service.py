# -*- coding: utf-8 -*-
from kubb_match.data.models import Round, GridPosition
from kubb_match.service.battle_service import BattleService
from kubb_match.service.knock_out_service import KnockOutService


class TournamentService(object):
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.battle_service = BattleService()
        self.knock_out_service = KnockOutService()

    def init_battle_phase(self, phase):
        round1 = Round()

        positions = []
        teams = self.data_manager.get_teams()
        t = 0
        for row in ('A', 'B', 'C', 'D', 'E'):
            for x in range(1, 9):
                key = row + str(x)
                team = teams[t]
                grid_pos = GridPosition(position=key, team_id=team.id)
                grid_pos.team = team
                t += 1
                positions.append(grid_pos)

        round1.positions = positions

        round1.games = self.battle_service.create_games(positions)

        phase.rounds.append(round1)
        self.data_manager.save(phase)
        return round1

    def next_battle_round(self, phase):
        prev_round = next((r for r in phase.rounds if not r.played))
        round = self.battle_service.calculate_next_round(prev_round)

        prev_round.played = True
        self.data_manager.save(prev_round)

        phase.rounds.append(round)
        self.data_manager.save(phase)
        return round

    def final_battle_round(self, phase):
        prev_round = next((r for r in phase.rounds if not r.played))
        final_round = self.battle_service.calculate_next_round(prev_round, final=True)
        final_round.final = True

        prev_round.played = True
        self.data_manager.save(prev_round)

        phase.rounds.append(final_round)
        self.data_manager.save(phase)
        return final_round

    def init_ko_phase(self, phase, final_positions):
        ko_rounds = self.knock_out_service.create_initial_rounds(final_positions)

        for round in ko_rounds:
            phase.rounds.append(ko_rounds[round])
        self.data_manager.save(phase)
        return ko_rounds

    def next_ko_round(self, phase):
        prev_ko_rounds = [r for r in phase.rounds if not r.played]
        field ={'A': 1, 'B': 9, 'C': 13, 'D': 17}
        for prev_round in prev_ko_rounds:
            prev_round.played = True
            self.data_manager.save(prev_round)
            round = self.knock_out_service.calculate_next_round(prev_round,
                                                                field[prev_round.label]) if not prev_round.final else prev_round
            round.label = prev_round.label
            phase.rounds.append(round)
        self.data_manager.save(phase)
        return phase.rounds

    def final_ko_round(self, phase):
        pass
