class A:
    def __init__(self):
        self.p = 2

    def x(self):
        A.m(self)

    def m(self):
        print('Tea')

t = A()
print(t.p)
t.x()
