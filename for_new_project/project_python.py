t = [1,3]
t += (4,2,1)
print(t)
""""""
# t = (1,2)
# t[0] = 3
# print(t)
'''TypeError: 'tuple' object does not support item assignment'''
""""""
# l = [1, 2, 3, 4, 5]
# print(l[1:6:2])
'''[2, 4]'''
""""""
# l = [1, 2, 3]
# for i in l:
#      if i < 4:
#         l.append(i + 3)
#
# print(l)
'''[1, 2, 3, 4, 5, 6]'''
""""""
# s = {x**2 for x in range(3)}
# s1 = [1,2,3,1,4]
#
# print(s[1])
'''TypeError: 'set' object is not subscriptable'''
""""""
# x = [1, 2, 3]
# y = x
# del x
# print(y)

""""""
# m = map(lambda x: x**2, filter(None, [0,1,2]))
# print(list(m))
# print(m)

""""""
# l = [1,2,3]
# v = l[:]
# v[0] = 4
# print(v)

""" """
# g = 1
# def func(a):
#     g=a
#     return g
#
# print(func(2))
# print(g)

""" """
# a = "text"
# a[4] = "T"
# print(a)