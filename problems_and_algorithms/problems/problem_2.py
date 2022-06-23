from typing import List


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
