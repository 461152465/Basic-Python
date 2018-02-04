> 需要总结的：各种函数、方法、特性
>
> Attention: 学习进行到一定进度的时候做Summary所用，并不是单纯的记录

### String 字符串

1. **Strip（）方法**：将字符串首尾特定的子串去掉

   ```python
   "   Smoke  ".strip() #去掉首尾的空格
   "00 Smoke  00".strip("0") #去掉首尾的“0”
   ```


2. **isspace()方法**：判断字符串是否只包含空格字符

### Print函数

1.  Python 3.x 默认最后是换行符

   ```python 
   print ("string",end="") #自定义print最后的输出
   ```

   ​

### 字典

1. items方法 ： 返回字典中的键值对 



### 其他

1. len函数

   ```python
   len('Hello') #return 5
   ```

2. 解包(Unpacking)



### 列表推导式 （list comprehension）





1. del语句：删除对象或者只是需要删除的名称

   ```python 
   x = 1
   del x 
   ```

2. pass语句：用于程序中的占位

3. exec（）函数：将字符串作为语句进行执行

   ```python
   exec ("print ('Hello,world')")
   ```

4. eval（）函数：将字符串作为语句执行，计算表达式的值

   ```python 
   eval('1+2')
   ```

