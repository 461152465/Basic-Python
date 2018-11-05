# 测试字典
dict = {'Name':'mio', 'Age':'20','Class':'First'}

print("dict['Name']",dict['Name'])
print("dict['Age']",dict['Age'])
print("\n")

dict['Age'] = 21
dict['School'] = 'DFS School'
print("dict['School']",dict['School'])
print("dict['Age']",dict['Age'])

del dict['Age']
print(dict)