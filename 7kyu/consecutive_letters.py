def solve(st):
    s = 'abcdefabcdefghijklmnopqrstuvwxyz'
    not_mod = sorted(st)
    mod = ''.join(not_mod)
    if mod in s:
        return True
    else:
        return False
a = solve('abbc')
print(a)