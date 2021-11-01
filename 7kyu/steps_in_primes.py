def step(g, m, n):
    for i in range(m, n):
        if is_prime(i) and is_prime(i + g):
            return [i, i + g]
        if i + g > n:
            return None


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


dig = is_prime(105)
print(dig)

it = step(5, 100, 110)
print('Answer', it)

'''True'''
