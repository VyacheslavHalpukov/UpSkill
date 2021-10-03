def inc(x):
    return x + 1

def test_inc():
    assert inc(3) == 4, 'Not Work'

class ClassT:

    def methods(self, y):
        return y*2

print(inc(20))

def test_class():
    t = ClassT()
    assert t.methods(2) == 4, 'Not Work'
    assert t.methods(3) == 6, 'NOT'

def test_class1():
    t = ClassT()
    assert t.methods(3) == 6, 'NOT'
