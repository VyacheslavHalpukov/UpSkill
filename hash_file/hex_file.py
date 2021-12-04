import hashlib

file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
hex_val = 255573495
bytes_From_int = hex_val.to_bytes(4, byteorder='big')
print(bytes_From_int)
file_hash.update(bytes_From_int)
key_one = file_hash.digest()
print(key_one.hex())


# int_hash = hashlib.sha256()
# int_hash.update(bytes_From_int)
# print(int_hash.digest().hex())
cor_str = True
int_h = 0
# int_b = int(hex_h, 16)

while cor_str:
    # int_hash = hashlib.new('ripemd160')
    int_hash = hashlib.sha256()

    print(key_one.hex(), int_hash.digest().hex())
    bytes_From_ans = int_h.to_bytes(4, byteorder='big')
    print(bytes_From_int, bytes_From_ans)
    int_h += 1
    # int_hash.update()
    int_hash.update(bytes_From_ans)
    print(int_h)
    if key_one == int_hash.digest():
        cor_str = False
    print(key_one.hex(), int_hash.digest().hex())


    # int_hash.update(byte_val)

# print(int_b)
# int_b +=  1
# hex_hh = hex(int_b)
# print(hex_hh)


# int_hash = hashlib.sha256()
# int_val = 253
#
# int_val += 1
# print(int_val)
# str_val = str(int_val)
# byte_val = str_val.encode()
# int_hash.update(byte_val)
# print(int_hash.digest().hex())
# print(byte_val)


# while int_hash.digest() != key_one:
#     int_val += 1
#     print(int_val)
#     str_val = str(int_val)
#     byte_val = str_val.encode()
#     int_hash.update(byte_val)
#     print(int_hash.digest().hex())
#     print(byte_val)