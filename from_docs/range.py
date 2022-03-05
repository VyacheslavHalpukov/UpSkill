def for_map(enter):
    return enter**2



u = (1,2,3)
z = map(for_map, u)

print(list(z))