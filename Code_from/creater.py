from Code_from.writer import from_file

class Create:

    @staticmethod
    def create_from():
        with open('writer.py', 'w') as f:
            f.write("def from_file(): print('Hello world!')")

p = Create.create_from()
exec(open('writer.py').read())
from_file()





