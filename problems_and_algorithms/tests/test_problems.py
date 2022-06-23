import unittest

from ..problems.problem_1 import sqrt
from ..problems.problem_2 import binary_search, get_pivot_index, linear_search, rotated_array_search
from ..problems.problem_3 import rearrange_digits
from ..problems.problem_4 import sort_012
from ..problems.problem_6 import get_min_max
from ..problems.problem_7 import Router


class TestProblems(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(3, sqrt(9))
        self.assertEqual(0, sqrt(0))
        self.assertEqual(4, sqrt(16))
        self.assertEqual(1, sqrt(1))
        self.assertEqual(5, sqrt(27))
        self.assertEqual(9, sqrt(99))
        self.assertEqual(316264, sqrt(100023042335))
        self.assertEqual(1000115205, sqrt(1000230423351234123))

    def test_binary_search(self):
        self.assertEqual(-1, binary_search([], 10, 0, 0))
        self.assertEqual(0, binary_search([10], 10, 0, 1))
        self.assertEqual(0, binary_search([6, 7, 8, 9, 10], 6, 0, 5))
        self.assertEqual(2, binary_search([1, 2, 3, 4], 3, 0, 4))
        self.assertEqual(2, binary_search([6, 7, 8], 8, 0, 3))
        self.assertEqual(-1, binary_search([4, 8, 10, 11, 30], 9, 0, 5))

    def test_get_pivot_index(self):
        rotated_list = [6, 7, 8, 9, 10, 1, 2, 3, 4]
        self.assertEqual(5, get_pivot_index(rotated_list, 0, len(rotated_list) - 1))

        rotated_list = [1, 2, 3, 4]
        self.assertEqual(0, get_pivot_index(rotated_list, 0, len(rotated_list) - 1))

        rotated_list = [6, 7, 8, 1]
        self.assertEqual(3, get_pivot_index(rotated_list, 0, len(rotated_list) - 1))

        rotated_list = [6, 7, 8, 1, 2, 3, 4]
        self.assertEqual(3, get_pivot_index(rotated_list, 0, len(rotated_list) - 1))

        rotated_list = []
        self.assertEqual(0, get_pivot_index(rotated_list, 0, 0))

        rotated_list = [10]
        self.assertEqual(0, get_pivot_index(rotated_list, 0, 0))

        rotated_list = [i * 4 for i in range(102, 200)] + [i * 4 for i in range(100)]
        self.assertEqual(98, get_pivot_index(rotated_list, 0, len(rotated_list) - 1))

    def test_rotated_array_search(self):
        rotated_list = [6, 7, 8, 9, 10, 1, 2, 3, 4]
        target = 6
        self.assertEqual(linear_search(rotated_list, target), rotated_array_search(rotated_list, target))

        rotated_list = [6, 7, 8, 9, 10, 1, 2, 3, 4]
        target = 1
        self.assertEqual(linear_search(rotated_list, target), rotated_array_search(rotated_list, target))

        rotated_list = [6, 7, 8, 1, 2, 3, 4]
        target = 8
        self.assertEqual(linear_search(rotated_list, target), rotated_array_search(rotated_list, target))

        rotated_list = [6, 7, 8, 1, 2, 3, 4]
        target = 1
        self.assertEqual(linear_search(rotated_list, target), rotated_array_search(rotated_list, target))

        rotated_list = [6, 7, 8, 1, 2, 3, 4]
        target = 10
        self.assertEqual(linear_search(rotated_list, target), rotated_array_search(rotated_list, target))

        rotated_list = []
        target = 10
        self.assertEqual(linear_search(rotated_list, target), rotated_array_search(rotated_list, target))

        rotated_list = [10]
        target = 10
        self.assertEqual(linear_search(rotated_list, target), rotated_array_search(rotated_list, target))

        rotated_list = [i * 4 for i in range(102, 200)] + [i * 4 for i in range(100)]
        target = 110 * 4
        self.assertEqual(linear_search(rotated_list, target), rotated_array_search(rotated_list, target))

    def test_rearrange_digits(self):
        self.assertEqual(sum(rearrange_digits([1, 2, 3, 4, 5])), sum([542, 31]))
        self.assertEqual(sum(rearrange_digits([4, 6, 2, 5, 9, 8])), sum([964, 852]))
        self.assertEqual(sum(rearrange_digits([1, 2])), sum([1, 2]))
        self.assertEqual(sum(rearrange_digits([1])), sum([1, 0]))
        self.assertEqual(sum(rearrange_digits([])), sum([0, 0]))
        self.assertEqual(sum(rearrange_digits([0, 2, 3, 4])), sum([40, 32]))

    def test_sort_012(self):
        input_list = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
        sorted_list = sorted(input_list)
        sort_012(input_list)
        self.assertEqual(input_list, sorted_list)

        input_list = []
        sorted_list = sorted(input_list)
        sort_012(input_list)
        self.assertEqual(input_list, sorted_list)

        input_list = [0, 0, 0]
        sorted_list = sorted(input_list)
        sort_012(input_list)
        self.assertEqual(input_list, sorted_list)

        input_list = [1, 1, 1]
        sorted_list = sorted(input_list)
        sort_012(input_list)
        self.assertEqual(input_list, sorted_list)

        input_list = [2, 2, 2]
        sorted_list = sorted(input_list)
        sort_012(input_list)
        self.assertEqual(input_list, sorted_list)

        input_list = [0]
        sorted_list = sorted(input_list)
        sort_012(input_list)
        self.assertEqual(input_list, sorted_list)

        input_list = [1]
        sorted_list = sorted(input_list)
        sort_012(input_list)
        self.assertEqual(input_list, sorted_list)

        input_list = [2]
        sorted_list = sorted(input_list)
        sort_012(input_list)
        self.assertEqual(input_list, sorted_list)

        input_list = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
        sorted_list = sorted(input_list)
        sort_012(input_list)
        self.assertEqual(input_list, sorted_list)

        input_list = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        sorted_list = sorted(input_list)
        sort_012(input_list)
        self.assertEqual(input_list, sorted_list)

    def test_get_min_max(self):
        self.assertTupleEqual(get_min_max([]), (None, None))
        self.assertTupleEqual(get_min_max([10]), (10, 10))
        self.assertTupleEqual(get_min_max([i for i in range(0, 10)]), (0, 9))
        self.assertTupleEqual(get_min_max([0, 0, 0, 0]), (0, 0))
        self.assertTupleEqual(get_min_max([124, 23, 3, -33, 3, -6, 43]), (-33, 124))
        self.assertTupleEqual(get_min_max([3, 2, 5, 1, 24, 6]), (1, 24))
        self.assertTupleEqual(get_min_max([1, 2, 3]), (1, 3))

    def test_router(self):
        # create the router and add a route
        router = Router("root handler",
                        "not found handler")  # remove the 'not found handler' if you did not implement this
        router.add_handler("/home/about", "about handler")  # add a route
        self.assertEqual(router.lookup("/"), 'root handler')
        self.assertEqual(router.lookup("/home"), 'not found handler')
        self.assertEqual(router.lookup("/home/about"), 'about handler')
        self.assertEqual(router.lookup("/home/about/"), 'about handler')
        self.assertEqual(router.lookup("/home/about/me"), 'not found handler')
