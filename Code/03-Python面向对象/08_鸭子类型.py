class Human:
    def eat(self):
        print('人类吃饭')

# 美国
class UsHuman(Human):
    def eat(self):
        print("美国人用叉子吃牛排")
        
        
class Dog():

    def eat(self):
        print("狗狗吃饭用盆")
        
    def run(self):
        print("狗狗跑")
        
def someone_eat(someone):
    print(someone, type(someone))
    someone.eat()
    
    if type(someone) == Dog:
        someone.run()
    
human = UsHuman()
someone_eat(human)

gousheng = Dog()
someone_eat(gousheng)