for i in range(5):
    print(i)
else:
    print('END')


class One:

    @classmethod
    def sum(self, a, b):
        return a + b


class Two(One):
    pass


o = One()
# b = Two()

k = Two.sum(2, 3)

p = One.sum(1, 2)

print(p, k)
