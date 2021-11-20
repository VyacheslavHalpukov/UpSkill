def generat_list(n):
    generat_arr = [i + 1 for i in range(n)]
    return generat_arr

def josephus_survivor(n, k):
    new_n = generat_list(n)
    i = 0
    result_arr = []
    while new_n:
        i = (i + k - 1) % len(new_n)
        result_arr += [new_n.pop(i)]
    return result_arr[len(result_arr) - 1]


num_cw = josephus_survivor(1774, 4070)
print(num_cw)
