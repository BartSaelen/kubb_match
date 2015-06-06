# -*- coding: utf-8 -*-
import unittest
from kubb_match.service.battle_service import BattleService


class BattleServiceTests(unittest.TestCase):
    def setUp(self):
        self.battle_service = BattleService()

    def test_move_row_up(self):
        row = self.battle_service.move_row_up('B')
        self.assertEqual('A', row)

    def test_move_row_up_another(self):
        row = self.battle_service.move_row_up('D')
        self.assertEqual('C', row)

    def test_move_row_down(self):
        row = self.battle_service.move_row_down('A')
        self.assertEqual('B', row)

    def test_move_row_down_another(self):
        row = self.battle_service.move_row_down('D')
        self.assertEqual('E', row)
