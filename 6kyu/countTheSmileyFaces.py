import itertools

lib_book = []
prod = itertools.product(':;', ')D')
prod_nose = itertools.product(':;', '-~', ')D')
for i in prod:
    lib_book.append(''.join(i))
for i in prod_nose:
    lib_book.append(''.join(i))


def count_smileys(arr):
    number_smiles = 0
    for i in arr:
        if i in lib_book:
            number_smiles += 1
    return number_smiles


z = count_smileys([';]', ':[', ';*', ':$', ';-D'])
print(z)