import hashlib

class Hash:

    def __init__(self, string_a=None):
        self.string = string_a

    def print_hw(self):
        id_l = hashlib.sha256(b'Hello world').hexdigest()
        return id_l, len(id_l)

    def get_hash(self):
        str_to_bytes = bytes(self.string, 'utf-8')
        hasg_object = hashlib.sha256(str_to_bytes)
        return hasg_object.hexdigest()

obj = Hash('Hd')
fr_om = obj.get_hash()
ideal, len = obj.print_hw()

print(fr_om)
print(ideal, len)
print(ideal)

