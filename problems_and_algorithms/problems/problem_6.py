from typing import List, Tuple
import unittest


def get_min_max(numbers: List[int]) -> Tuple[int, int]:
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(numbers) == 0:
        return (None, None)

    min_number = float('inf')
    max_number = float('-inf')
    for number in numbers:
        min_number = min(min_number, number)
        max_number = max(max_number, number)

    return min_number, max_number


class TestProblems(unittest.TestCase):

    def test_get_min_max(self):
        self.assertTupleEqual(get_min_max([]), (None, None))
        self.assertTupleEqual(get_min_max([10]), (10, 10))
        self.assertTupleEqual(get_min_max([i for i in range(0, 10)]), (0, 9))
        self.assertTupleEqual(get_min_max([0, 0, 0, 0]), (0, 0))
        self.assertTupleEqual(get_min_max([124, 23, 3, -33, 3, -6, 43]), (-33, 124))
        self.assertTupleEqual(get_min_max([3, 2, 5, 1, 24, 6]), (1, 24))
        self.assertTupleEqual(get_min_max([1, 2, 3]), (1, 3))


if __name__ == '__main__':
    print('running tests')
    try:
        unittest.main(argv=[''], verbosity=3, exit=False)
        print('tests passed')
    except:
        print('tests failed')
