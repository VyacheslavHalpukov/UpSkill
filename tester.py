class Test:
    # class test
    def __init__(self, track):
        self.test = 'Mouse'
        self.track = track

    def print_1(self, num: int, eggs: str = 'eggs'):
        return num

    @staticmethod
    def print_simple(a, b):
        return a + b

    def print_track(self):
        return self.track



tes = Test(1)
print(tes.print_1(1))
print(Test.print_simple(1, 200))

class Test1(Test):

    # Next generate class
    def __init__(self, track):
        super().__init__(track)

tes1 = Test1(12)
print(Test1.print_simple(22, 44))

print(tes1.print_track())
