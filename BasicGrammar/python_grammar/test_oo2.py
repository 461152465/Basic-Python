# 测试面向对象
class Person:
    def __init__(self,name):
        self.name = name

    def sayhello(self):
        print('My name is',self.name)

p = Person('mio')
print(p.name)