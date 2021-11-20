def josephus_survivor(n, k):
    new_arr = []
    const_arr = [i + 1 for i in range(n)]


    def insert_josephus(n,k):

        if k == 1:
            return n
        elif len(n) > k:
            prom = n[k:] + n[:k - 1]
            # print(prom, n[k-1])
            new_arr.append(n[k-1])
            return (insert_josephus(prom, k))
        elif len(n) == k:
            prom = n[:-1]
            # print(prom, n[k-1])
            new_arr.append(n[k - 1])
            return (insert_josephus(prom, k))
        elif len(n) < k and len(n) > 1:
            koef = k
            while koef - len(n) > len(n):
                koef = koef - len(n)


            new_k = koef - len(n)
            firest_step = n[new_k:]
            second_step = n[:new_k - 1]
            prom = n[new_k:] + n[:new_k - 1]
            # print(prom, n[new_k-1])
            new_arr.append(n[new_k - 1])
            return (insert_josephus(prom, k))
        # TODO The recursion must be removed from this method.
        else:
            # print(n)
            new_arr.append(n[0])
            return new_arr
    if n == []:
        return 0
    else:
        out = insert_josephus(const_arr, k)
        return out[len(out)-1]


out = josephus_survivor(7, 3)
print(out)

# f = inita([1,2,3,4,5,6,7,8,9,10,11], 3)
# print(f)