import array
# задача 2 Объяснить почему переменная "a", "с", "d" , не изменились, а переменная "b", изменилась
a = 0
b = []
c = []
d = 'a'


def func_a(a):
    a += 1



def func_b(b):
    b += [1,2]

    print(b)



def func_c(c):
    c = [2]


def func_d(d):
    d += 'd'


func_a(a)
func_b(b)
func_c(c)
func_d(d)
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
b = [3]
print(f'b = {b}')