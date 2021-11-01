def solve(s):
    dictionary = ['a', 'e', 'i', 'o', 'u']
    # 'y' is not from upper list
    long = 0
    tup_long = []
    for i,j in enumerate(s):
        if j in dictionary:
            long += 1
            tup_long.append(long)
        else: long = 0
    return max(tup_long)

print(solve('teseet'))