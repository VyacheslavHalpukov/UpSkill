# def josephus_survivor(n,k):
#
#     init_sequance = [i for i in range(1, n + 1)]
# new_arr = []

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
            new_k = k - len(n)
            prom = n[new_k:] + n[:new_k - 1]
            # print(prom, n[new_k-1])
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

# return inita(init_sequance, k)



out = josephus(["C","o","d","e","W","a","r","s"],4)
print(out)

# f = inita([1,2,3,4,5,6,7,8,9,10,11], 3)
# print(f)