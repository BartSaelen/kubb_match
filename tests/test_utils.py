# -*- coding: utf-8 -*-
import unittest
from kubb_match.utils import move_row_up, move_row_down


class UtilTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_move_row_up(self):
        row = move_row_up('B')
        self.assertEqual('A', row)

    def test_move_row_up_another(self):
        row = move_row_up('D')
        self.assertEqual('C', row)

    def test_move_row_down(self):
        row = move_row_down('A')
        self.assertEqual('B', row)

    def test_move_row_down_another(self):
        row = move_row_down('D')
        self.assertEqual('E', row)
