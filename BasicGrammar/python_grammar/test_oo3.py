class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()
print("\n")

class Test2:
    def prt(mio):
        print(mio)
        print(mio.__class__)

t2 = Test2()
t2.prt()