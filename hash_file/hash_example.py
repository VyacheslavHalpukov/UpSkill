import hashlib

file = "ava.jpeg" # Location of the file (can be set a different way)
BLOCK_SIZE = 4 # The size of each read from the file

file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
len_file = 0
with open(file, 'rb') as f: # Open the file to read it's bytes
    fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
    # print(fb)
    while len(fb) > 0: # While there is still data being read from the file
        print(fb.hex())
        len_file += 1
        file_hash.update(fb) # Update the hash
        fb = f.read(BLOCK_SIZE) # Read the next block from the file

print (file_hash.hexdigest()) # Get the hexadecimal digest of the hash
print(len_file)