class SomeClass(object):
    pass

"""Можно добавить методы в класс уже после создания класса"""

def squareMethod(self, x):
    return x*x
# SomeClass.square = squareMethod
"""И не важно перед созданием объекта добавлять или после"""
obj = SomeClass()
SomeClass.square = squareMethod
p = obj.square(5) # 25
print(p)

"""
25
"""
