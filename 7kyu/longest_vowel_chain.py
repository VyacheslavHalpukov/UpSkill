def solve(s):
    dictionary = 'euioa'
    # 'y' is not from upper list
    # cant change this string in dictionary and rutern in other
    long = 0
    tup_long = []
    for i,j in enumerate(s):
        if j in dictionary:
            long += 1
            tup_long.append(long)
        else: long = 0
    return max(tup_long)

print(solve('teseet'))