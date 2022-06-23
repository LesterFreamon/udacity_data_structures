from typing import List, Tuple


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
