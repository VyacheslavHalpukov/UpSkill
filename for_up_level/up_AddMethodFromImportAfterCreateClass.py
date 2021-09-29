from up_addMethodInClass import SomeClass


def sum_method(self, x):
    """Method add after created Class"""
    return x + x

obj = SomeClass()
SomeClass.sum = sum_method

p = obj.sum(2)
print(p)