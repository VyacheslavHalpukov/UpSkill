class A:
    pass

class B(A):
    a = 'Test'
    def lay_eggs(self):
        return True

    pass

class C(A):
    def lay_eggs(self):
        print(self.a)
    pass

class D(C,B):
    # print(a)
    pass

d = D()
d.lay_eggs()