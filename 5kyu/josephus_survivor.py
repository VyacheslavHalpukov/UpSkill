def josephus(n, k):
    new_arr = []


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
            print(prom, n[new_k-1])
            new_arr.append(n[new_k - 1])
            return (insert_josephus(prom, k))
        else:
            # print(n)
            new_arr.append(n[0])
            return new_arr
    if n == []:
        return n
    else:
        out = insert_josephus(n, k)
        return out


out = josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],11)
print(out)

# f = inita([1,2,3,4,5,6,7,8,9,10,11], 3)
# print(f)