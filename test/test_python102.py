import pytest
import numpy as np
from exercises.python102 import (remove_duplicates, letter2words_histogram, return_swapped_parameters,
                                 module_caller, package_caller, setup_chessboard_with_colors)

class TestExercise_P10:
    def test_module(self):
        assert module_caller(), "It seems that module was not imported correctly"

class TestExercise_P11:
    def test_package(self):
        assert package_caller(), "It seems that package was not imported correctly"


class TestExercise_P12:

    @pytest.mark.parametrize("a,b",
                             [([2, 3, 1, 3, 5, 1], [2, 3, 5, 1]),
                              ([[4, 5, 2], [3, 4], [4, 5, 2], [1, 2]], [[3, 4], [4, 5, 2], [1, 2]])
                              ])
    def test_remove_duplicate(self, a, b):
        a_copy = a[:]
        remove_duplicates(a_copy)
        for x in b:
            a_copy.remove(x)
        if not a_copy == []:
            pytest.fail("The method 'remove_duplicates' failed with argument {}.\n"
                        "The result should have been {}, it was {}".format(a, b, a_copy))

    def test_none(self):
        assert remove_duplicates([1, 2, 3]) == None, "Function remove_duplicates should return None"

# There is no test for exercise P13

# There is no test for exercise P14

class TestExercise_P15:

    @pytest.mark.parametrize("a,b",
                             [
                                 ("house",
                                  {'h': {'house'}, 'o': {'house'}, 'u': {'house'}, 's': {'house'}, 'e': {'house'}}
                                  ),
                                 ("it is", {'i': {'is', 'it'}, 't': {'it'}, 's': {'is'}})
                             ])
    def test_letter_2_word(self, a, b):
        result = letter2words_histogram(a)
        if not result == b:
            pytest.fail("The method 'letter2words_histogram' failed with argument '{}'.\n"
                        "The result should have been '{}', it was '{}'".format(a, b, result))


class TestExercise_P16:

    @pytest.mark.parametrize("a,b",
                             [
                                 ((2, 3), (3, 2)),
                                 (([2, 3], "mouse"), ("mouse", [2, 3]))
                             ])
    def test_swap(self, a, b):
        result = return_swapped_parameters(a[0], a[1])
        if not result == b:
            pytest.fail("The method 'return_swapped_parameters' failed with argument '{}'.\n"
                        "The result should have been '{}', but was '{}'".format(a, b, result))


class TestExercise_P17:
    """
    Test case for the chess board
    """
    def test_chessboard_setup(self):
        chessboard = setup_chessboard_with_colors()

        # Check the dimensions of the chessboard
        assert chessboard.shape == (8, 8), "Chessboard should be 8x8"

        # Check for the correct number of each piece
        # Assuming uppercase for white pieces and lowercase for black pieces
        assert np.count_nonzero(chessboard == 'R') == 2, "There should be 2 white rooks (R)"
        assert np.count_nonzero(chessboard == 'r') == 2, "There should be 2 black rooks (r)"
        assert np.count_nonzero(chessboard == 'N') == 2, "There should be 2 white knights (N)"

        # Check specific positions (e.g., kings and queens)
        assert chessboard[0, 4] == 'k', "Black king (k) should be at position 0, 4"
        assert chessboard[7, 4] == 'K', "White king (K) should be at position 7, 4"

class TestExercise_P18:
    """
    Test case for tetris high scores
    """
    def test_read_csv(self):
        pass