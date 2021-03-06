import pytest
from validator import validate


class TestValidator(object):
    def test_validate_is_true(self):
        assert True == validate([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                 [3, 4, 5, 2, 8, 6, 1, 7, 9]])

    def test_validate_invalid_in_horizontal(self):
        assert False == validate([[5, 3, 4, 6, 7, 8, 9, 1, 5],
                                  [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                  [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                  [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                  [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                  [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                  [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                  [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                  [3, 4, 5, 2, 8, 6, 1, 7, 9]])

    def test_validate_invalid_in_vertical(self):
        assert False == validate([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                  [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                  [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                  [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                  [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                  [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                  [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                  [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                  [5, 4, 5, 2, 8, 6, 1, 7, 9]])

    def test_validate_invalid_in_block(self):
        assert False == validate([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                  [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                  [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                  [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                  [5, 6, 7, 8, 9, 1, 2, 3, 4],
                                  [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                  [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                  [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                  [9, 1, 2, 3, 4, 5, 6, 7, 8]])
