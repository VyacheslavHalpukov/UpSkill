z = [x for x in range(3)]
v = {x for x in range(10)}
a = iter(z)
print(next(a))
print(next(a))
print(next(a))
b = iter(z)
print(next(b))
# for i in z:
#     print(i)
# print(v)
# print(z)
# print(next(z))
# print(next(z))
# d = iter(z)
# print(next(d))

# a = [1]
# def f(a):
#     print (a)
#     a.extend([2])
#     print (a)
#
# print (a)
# print (f(a))
# print (a)
# print(type(a))