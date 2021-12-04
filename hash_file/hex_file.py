import hashlib

file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
file_hash.update(b'Argument')
file_hash.digest()

print(file_hash.digest())
