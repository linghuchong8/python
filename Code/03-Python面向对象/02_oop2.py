# 1.声明Person类
class Person:
    
    def __init__(self, name, age):
        """初始化方法，构造方法 """
        self.name = name
        self.age = age
        print("init方法被调用, 对象被创建", name)

    def eat(self):
        """eat方法"""
        print(self.name, "吃饭")
        
    def run(self):
        """run方法"""
        print(self.name, "跑步")
        
    def say_hello(self, target):
        print(self.name, "say hello to", target)
        
    # 格式： 姓名->xx,年龄->xx (重写、覆写__str__方法)
    def __str__(self) -> str:
        return "姓名->{}, 年龄->{}".format(self.name, self.age)
        
# 2.创建对象(初始化对象的属性)
p = Person("桑尼", 12)
# 调用对象的方法(self参数不需要传，self代表调用方法的对象)
p.eat()
p.run()
p.say_hello("小蓝")

print(p)
print("-----------------------")

p2 = Person("小红", 14)
p2.eat()
p2.run()

print(p2)