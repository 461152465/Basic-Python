# 测试面向对象
class Employee:
    '员工类定义'
    empCount = 0 #empCount是类变量
    def __init__(self,name,salary): #Python构造函数
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self): #第一个参数都是self，表示实例
        print('Total Employee %d'% Employee.empCount)
    def displayEmployee(self):
        print('name',self.name,',salary',self.salary)

e1 = Employee('mio',1000)
e2 = Employee('mio2',2000)
print(e1.empCount)