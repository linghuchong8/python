"""
导入模块中部分功能, 只导入add函数，Person类

from 模块名 import 函数,变量,类
"""

from utils import add, Person

print(add(3, 5))

p = Person("张三", 15)
print(p)