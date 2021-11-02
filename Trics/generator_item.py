import itertools

lib_book = []
prod = itertools.product(':;', ')D')
prod_nose = itertools.product(':;', '-~', ')D')
for i in prod:
    lib_book.append(''.join(i))
for i in prod_nose:
    lib_book.append(''.join(i))

print(lib_book)
# print(next(prod))
shema = (';)')
if shema in lib_book:
    print('Yess')

"""[':)', ':D', ';)', ';D', ':-)', ':-D', ':~)', ':~D', ';-)', ';-D', ';~)', ';~D']"""
