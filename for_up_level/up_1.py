for i in range(5):
    print(i)
else:
    print('END')

class One:

    def sum(self,a,b):
        return a+b

class Two(One):
    pass

o = One()
b= Two()

k = b.sum(2,3)

p = o.sum(1,2)

print(p, k)
