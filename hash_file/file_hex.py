int_a = 8
hex_h = '00'
int_b = int(hex_h, 16) + int('1')


print(int_b)
int_b +=  1
hex_hh = hex(int_b)
print(hex_hh)