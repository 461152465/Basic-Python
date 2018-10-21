# 测试异常
"""
Python和Javascript都是弱类型语言，变量类型不需要声明
Python中的标准类型：
1.数字
2.字符串
3.元组
4.列表
5.字典
"""

'''
Python中的True大写
while和try之后有:
'''

while True:
    try:
        x = int(input("Please enter a number:"))
        #str(x)：int转string类型
        print('the number you input:' + str(x))
        break
    except ValueError:
        print("That was no valid number,please try again")