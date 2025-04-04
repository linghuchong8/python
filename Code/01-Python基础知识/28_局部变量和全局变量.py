# 全局变量
m = 123

def func1():
    # 局部变量
    a = 10
    
    # 如果需要修改全局变量，先通过global关键字声明
    global m
    m = 222
    
    print("a =", a)
    print("m =", m)
    
    
def func2():
    # 局部变量
    a = 20
    
    print("a =", a)
    print("m =", m)
    

func1()
func2()