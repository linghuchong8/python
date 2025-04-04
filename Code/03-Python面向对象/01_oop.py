# 1.声明Person类
class Person:
    
    def __init__(self, name, age):
        """初始化方法，构造方法
        :param name: 姓名
        :param age: 年龄
        """
        self.name = name
        self.age = age
        print("init方法被调用, 对象被创建")

    def eat(self):
        """eat方法"""
        print(self.name, "吃饭")
        
    def run(self):
        """run方法"""
        print(self.name, "跑步")
        
# 2.创建对象(初始化对象的属性)
p = Person("桑尼", 12)
# 调用对象的方法(self参数不需要传，self代表调用方法的对象)
p.eat()
p.run()

print(p)