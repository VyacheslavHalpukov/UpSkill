import array as ar
a = [1,2,3]
b = ar.array('i', [1,2,3])

a[0] = 0
b[0] = 34
print(b[0])