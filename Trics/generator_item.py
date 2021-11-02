import itertools
lib_book = []
prod = itertools.product(':;', ')D', repeat = 1)
for i in prod:
    lib_book.append(''.join(i))

print(lib_book)
# print(next(prod))
shema = (';)')
if shema in lib_book:
    print('Yess')