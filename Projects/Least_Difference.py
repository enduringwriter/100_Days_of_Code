# Least Difference

print('Least Difference b/t any 2 numbers among abc', end="\n")


def least_difference(a, b, c):
    """ Return the smallest diffrence between
    any two numbers among a, b, c.
    >>> least_difference (1, 5, -5)
    4
    """
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    return min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
    sep="\n", end="\n")

help(least_difference)
