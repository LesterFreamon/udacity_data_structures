import heapq
from typing import List
import unittest


def rearrange_digits(input_list: List[int]) -> List[int]:
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return [0, 0]

    multiply = 1
    heapq.heapify(input_list)
    first_number = 0
    second_number = 0
    while len(input_list) > 1:
        first_number += multiply * heapq.heappop(input_list)
        second_number += multiply * heapq.heappop(input_list)
        multiply *= 10

    if len(input_list) == 1:
        first_number += multiply * heapq.heappop(input_list)

    return [first_number, second_number]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


class TestProblems(unittest.TestCase):

    def test_rearrange_digits(self):
        self.assertEqual(sum(rearrange_digits([1, 2, 3, 4, 5])), sum([542, 31]))
        self.assertEqual(sum(rearrange_digits([4, 6, 2, 5, 9, 8])), sum([964, 852]))
        self.assertEqual(sum(rearrange_digits([1, 2])), sum([1, 2]))
        self.assertEqual(sum(rearrange_digits([1])), sum([1, 0]))
        self.assertEqual(sum(rearrange_digits([])), sum([0, 0]))
        self.assertEqual(sum(rearrange_digits([0, 2, 3, 4])), sum([40, 32]))


if __name__ == '__main__':
    print('running tests')
    try:
        unittest.main(argv=[''], verbosity=3, exit=False)
        print('tests passed')
    except:
        print('tests failed')
