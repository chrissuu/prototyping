
def rationals(r):
    """
    generates the positive rationals with no duplicates.
    """
    while True:
        r = (r[1], (r[1] * (r[0] // r[1])) + (r[1] - (r[0] % r[1])))
        return r


