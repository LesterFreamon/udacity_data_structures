from typing import List
import unittest

def binary_search(sorted_list: List[int], target: int, l_i: int, h_i: int) -> int:
    """Find the index of the target in a sorted list.

    Args:
       sorted_list(array): A sorted array to search
       target(int): The target
       l_i: the lower bound index
       h_i: the higher bound index (exclude)
    Returns:
       int: Index or -1
    """
    if l_i >= h_i:
        return -1

    if (target < sorted_list[l_i]) or (target > sorted_list[h_i - 1]):
        return -1

    m_i = (l_i + h_i) // 2
    m_num = sorted_list[m_i]
    if m_num == target:
        return m_i
    elif m_num < target:
        return binary_search(sorted_list, target, m_i + 1, h_i)
    else:
        return binary_search(sorted_list, target, l_i, m_i)


def get_pivot_index(rot_array: List[int], l_i: int, h_i: int) -> int:
    """
    Find the pivot index in a rotated sorted array

    Args:
        rot_array(array): A sorted array that was rotated
        l_i: the lower bound index
        h_i: the higher bound index (included)
    Returns:
        Index (int)
    """
    if l_i == h_i:
        return l_i

    l_n = rot_array[l_i]
    h_n = rot_array[h_i]
    if l_i + 1 == h_i:
        return l_i if l_n < h_n else h_i

    if l_n < h_n:
        return l_i

    m_i = (l_i + h_i) // 2
    m_n = rot_array[m_i]
    if m_n >= l_n:
        return get_pivot_index(rot_array, m_i + 1, h_i)
    else:
        return get_pivot_index(rot_array, l_i + 1, m_i)


def rotated_array_search(input_list: List[int], number: int) -> int:
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1

    pivot_index = get_pivot_index(input_list, 0, len(input_list) - 1)
    target_index = binary_search(input_list, number, 0, pivot_index)
    if target_index != -1:
        return target_index

    return binary_search(input_list, number, pivot_index, len(input_list))


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def _test_function():
    assert -1 == binary_search([], 10, 0, 0)
    assert 0 == binary_search([10], 10, 0, 1)
    assert 0 == binary_search([6, 7, 8, 9, 10], 6, 0, 5)
    assert 2 == binary_search([1, 2, 3, 4], 3, 0, 4)
    assert 2 == binary_search([6, 7, 8], 8, 0, 3)
    assert -1 == binary_search([4, 8, 10, 11, 30], 9, 0, 5)


class TestProblems(unittest.TestCase):

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


if __name__ == '__main__':
    print('running tests')
    try:
        unittest.main(argv=[''], verbosity=3, exit=False)
        print('tests passed')
    except:
        print('tests failed')
