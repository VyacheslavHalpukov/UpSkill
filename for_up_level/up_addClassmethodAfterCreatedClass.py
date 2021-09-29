class SomeClass(object):
    pass

"""Можно добавить методы в класс уже после создания класса"""
@classmethod
def squareMethod(cls, x):
    return x*x
# SomeClass.square = squareMethod
"""И не важно перед созданием объекта добавлять или после"""

SomeClass.square = squareMethod
p = SomeClass.square(5) # 25
print(p)

"""
25
"""