def solve(s):
    flag = len(s)/2
    num = 0
    for i in s :
        if i.isupper():
            num += 1
    if num <= flag:
        return s.lower()
    else:
        return s.upper()


a = solve('CodE')
print(a)