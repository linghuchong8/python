import random

# 无参无返回值
def say_hello():
    print("hello")
    
# 无参有返回值
def get_rand():
    # [0, 1)
    return random.random()

# 有参无返回值
def say_hi(name) -> None:
    print("你好：", name)
    
# 有参有返回值(返回类型通常省略)
def sum(a, b) -> int:
    return a + b
    
say_hello()
print(get_rand())
print(say_hi("菲菲"))
print(sum(3, 5))