# 字符串类型
name = "张三"
# 整型变量
age = 18
# 浮点类型变量
height = 175.6
# 布尔类型
handsome = True
# 复数类型 i^2 = -1
a = 1+2j

# 自动推断类型
print(name, type(name))         # str   -> string
print(age, type(age))           # int   -> integer
print(height, type(height))     # float
print(handsome, type(handsome)) # bool  -> boolean
print(a, type(a))

# 动态修改类型（改值）
height = 190
print("身高", height, type(height))     # float
age = 18.5
print("年龄", age, type(age))

print("--------------------------------------------- 变量名")
# 合法变量名
my_user_name = "abc"
myUserName   = "zhangsan"
MYUSERNAME   = "lisi"
print(myUserName)
print(MYUSERNAME)
# 非法的变量名
# 123name = "abc"
# user-name = "abc"
# for = "abc"
# itheima.com = "abc"


