"""
唐老鸭继承Animal的所有属性和方法
实现了其他父类的能力
- 飞行能力
- 游泳能力
- 说话能力
"""

class 动物:
    
    def __init__(self, name) -> None:
        self.name = name
        
    def 吃饭(self):
        print(f"{self.name} 在吃饭.") # f -> format
        
    def 睡觉(self):
        print(f"{self.name} 在睡觉.")
        
    def 游泳(self):
        print(f"{self.name} is swimming.")
        
class 飞行能力:
    
    def 翱翔(self):
        print(f"{self.name} 在飞行.")
        
class 游泳能力:
    
    def 游泳(self):
        print(f"{self.name} 在游泳.")
        
class 鸭子(动物, 飞行能力, 游泳能力):
    
    def __init__(self, name, color) -> None:
        super().__init__(name)
        self.color = color
        
        
唐老鸭 = 鸭子("唐老鸭1号", "红白色")
唐老鸭.吃饭()
唐老鸭.睡觉()
唐老鸭.翱翔()
唐老鸭.游泳()