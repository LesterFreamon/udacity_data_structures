import heapq
from typing import List


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
