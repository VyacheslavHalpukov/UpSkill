class Test:
    # class test
    def __init__(self):
        self.test = 'Mouse'

    def print(self, num:int, eggs: str = 'eggs'):
        return num

tes = Test()
print(tes.print(1))