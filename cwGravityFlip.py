def flip (d, a):
    # Returns the sorting depending on the flag
    if d == 'R':
        a = sorted(a)
        return a
    else:
        a = sorted(a, reverse=True)
        return a


print(flip('R', [3, 2, 1, 2]))
