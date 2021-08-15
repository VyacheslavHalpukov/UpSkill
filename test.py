class Test:
    # class test
    def __init__(self):
        self.test = 'Mouse'

    def print(self, num:int, eggs: str = 'eggs'):
        return num

    @staticmethod
    def print_simple(a, b):
        return a + b


tes = Test()
print(tes.print(1))
print(Test.print_simple(1, 20))
