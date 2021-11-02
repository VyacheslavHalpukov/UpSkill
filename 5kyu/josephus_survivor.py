def josephus_survivor(n,k):

    init_sequance = [i for i in range(1, n + 1)]
    for i in range(n):
        pass
        # TODO Think about logic maybe recursive

    if len(init_sequance) == 1:
        return init_sequance[0]
    else:
        return None


out = josephus_survivor(7,3)
print(out)