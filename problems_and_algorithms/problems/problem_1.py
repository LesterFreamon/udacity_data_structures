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
