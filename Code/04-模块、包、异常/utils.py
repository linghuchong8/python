"""
工具类
"""
# 定义变量
NAME = "张三"

# 定义函数
def add(a, b):
    return a + b


# 定义类
class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return 'name:{},age:{}'.format(self.name,self.age)