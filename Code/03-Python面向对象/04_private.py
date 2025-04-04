#圆类，计算圆周长

class Circle:
    
    def __init__(self, radius):
        # 初始化 attribute 属性
        # 半径
        self.radius = radius
        # PI 私有 
        self.__PI = 3.1415926
        # 计算次数记录
        self.__cnt = 0
        
    def perimeter(self):
        self.__count()
        # 2πr
        return 2 * self.__PI * self.radius
    
    def __count(self):
        self.__cnt += 1
        
    def __str__(self) -> str:
        return "calc: {}".format( self.__cnt)
    
c1 = Circle(10)
c1.radius = 1
# 私有化属性：不能强行修改，强改不会生效
# c1.__PI = 10
# 无法直接读取，直接读取，报错AttributeError: 'Circle' object has no attribute '__PI'
# print(c1.__PI)
print(c1.perimeter())
print(c1.perimeter())
print(c1.perimeter())
# 私有化方法：不能强行调用
# c1.__count()
print(c1)