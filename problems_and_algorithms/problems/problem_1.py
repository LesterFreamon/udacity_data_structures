import unittest


def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if (number == 0) or (number == 1):
        return number

    top_num = number // 2
    min_num = 1
    run_num = min_num + ((top_num - min_num) // 2)

    while True:
        run_num_square = run_num * run_num
        if run_num_square == number:  # we got the number
            return run_num
        elif run_num_square < number and ((run_num + 1) ** 2 > number):  # n^2 is too small, yet (n+1)^2 is too big
            return run_num
        elif run_num_square < number:  # n^2 is too small, so decrease the search space by cutting top_num
            min_num = run_num
            run_num = run_num + ((top_num - run_num) // 2)
        elif (run_num_square > number) and ((run_num - 1) ** 2 <= number):  # n^2 is too big, yet (n-1)^2 is too small
            return run_num - 1
        else:  # n^2 is too big, so decrease the search space by increasing min_num
            top_num = run_num
            run_num = run_num - ((run_num - min_num) // 2)


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


if __name__ == '__main__':
    print('running tests')
    try:
        unittest.main(argv=[''], verbosity=3, exit=False)
        print('tests passed')
    except:
        print('tests failed')
