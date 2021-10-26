a = [1]
def f(a):
    print (a)
    a.extend([2])
    print (a)

print (a)
print (f(a))
print (a)
print(type(a))