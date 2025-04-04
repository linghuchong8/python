"""-------------------------定义Person类（基类/父类）--------------------------
所有的class默认直接或间接地继承object
"""
class Person:
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def eat(self):
        print(self.name, "eat")
        
    def say_hello(self, target):
        print("{} say hello to {}".format(self.name, target))
        
"""-------------------------定义Student类（子类）--------------------------"""
class Student(Person):
    
    def __init__(self, name, age, score):
        # 调用父类的初始化方法
        super().__init__(name, age)
        # 定义自己的属性
        self.score = score
        
    def study(self):
        print("{}正在学习,得分:{}!".format(self.name, self.score))
        
# 创建学生对象
xiaoming = Student("小明", 16, 95)
# 访问自己和父类的属性
print("name:{} age:{} score:{}".format(xiaoming.name, xiaoming.age, xiaoming.score))
# 访问自己和父类的方法
xiaoming.study()
xiaoming.eat()
xiaoming.say_hello("老师")