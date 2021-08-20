def find_next_square(sq):
    sqrt = int(sq ** (0.5))
    if sqrt ** 2 == sq:
        return (sqrt + 1) ** 2
    else:
        return -1


print(find_next_square(625))
