def josephus_survivor(n,k):
    x = 0
    init_sequance = [i for i in range(1, n+1)]
    while x < 15:
        z = init_sequance.pop(3)
        print(x, z)
        x += 1
    return init_sequance

out = josephus_survivor(7,3)
print(out)