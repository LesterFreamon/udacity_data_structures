from typing import List
import unittest


def swap(arr: List[int], i: int, j: int) -> None:
    """Swap two elements of a given array according the the passed indecies

     Args:
       arr(list): A list
       i: first index
       j: second index
    """
    arr[i], arr[j] = arr[j], arr[i]


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    num_zeros_found, num_ones_found = 0, 0
    r_i = 0
    while r_i < len(input_list):
        this_num = input_list[r_i]
        if this_num == 0:
            swap(input_list, r_i, num_zeros_found + num_ones_found)
            swap(input_list, num_zeros_found + num_ones_found, num_zeros_found)
            num_zeros_found += 1
        elif this_num == 1:
            swap(input_list, r_i, num_zeros_found + num_ones_found)
            num_ones_found += 1
        else:
            pass
        r_i += 1


class TestProblems(unittest.TestCase):

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


if __name__ == '__main__':
    print('running tests')
    try:
        unittest.main(argv=[''], verbosity=3, exit=False)
        print('tests passed')
    except:
        print('tests failed')
