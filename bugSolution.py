def function_with_uncommon_error_solution(x, y):
    if x == 0 and y == 0:
        return float('nan')  # or raise an exception, depending on requirement
    elif x == 0:
        raise ZeroDivisionError("x cannot be zero")
    return y / x