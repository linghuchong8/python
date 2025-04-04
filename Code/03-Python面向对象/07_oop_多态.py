"""
多态案例

super()可以得到父类对象，调用父类的方法和属性
"""

# 父类
class Human:
    
    def eat(self):
        print("人类吃饭")
        
# 中国
class ZhHuman(Human):
    
    def eat(self):
        print("中国人用筷子吃米饭")
        
# 美国
class UsHuman(Human):
    
    def eat(self):
        print("美国人用叉子吃牛排")
    
# 非洲人
class AfricaHuman(Human):
    
    def eat(self):
        print("非洲人用手抓恩希玛")
    
# 函数
def someone_eat(human: Human):
    # 传递一个具备eat功能的对象(所有Human的子类都可以传进来，都有eat方法)
    human.eat()
    
zgr = ZhHuman()
mgr = UsHuman()
fzr = AfricaHuman()

print("---------------------")

someone_eat(zgr)
someone_eat(mgr)
someone_eat(fzr)