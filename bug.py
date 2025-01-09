def function_with_uncommon_error(x, y):
    if x == 0:
        return 0  # This is a problem in some cases if y is also zero 
    return y / x