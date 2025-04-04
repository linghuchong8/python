def say_hello():
    """打招呼
    """
    print("say hello")
    print("say hello")
    print("say hello")
    
def sum(a, b):
    """求两个数值和
    :param a: 第一个数
    :param b: 第二个数
    :return: 两数只和
    """
    return a + b
    
def my_min(a, b):
    """求两个数的最小值
    """
    if a < b:
        return a
    else:
        return b
    
def calc(a, b):
    """返回a和b的积和商
    
    None特殊的类型，意思为空，占位置用
    """
    multiply = a * b            # 乘法结果
    if b == 0:
        return multiply, None
    
    divide = a / b              # 除法结果
    return multiply, divide     
    
say_hello()
print(sum(3, 5))
print(sum(3, 5.2))
print(sum("abc", "haha"))
print(my_min(3, 2))
print(calc(7, 0))