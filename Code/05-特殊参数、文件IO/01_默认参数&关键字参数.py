def say_hello(score, name="刘亦菲"):
    # 默认参数：如果name（形参）没有对应的实参传入，则使用默认值
    # 默认参数要放最后
    # 非默认参数，必须有实参，否则报错
    # score : positional argument 必传
    # name  : default argument 可传
    print(f"Hello: {name} score: {score}")
    
def show_info(name, age=18, height=165.0):
    print(f"姓名: {name} 年龄: {age} 身高: {height}")
    
say_hello(41, "高圆圆")
say_hello(35) # positional argument: 'name'

# 可以使用形参的参数名作为关键字
show_info("张三", 16, 170)
show_info("张三", age=13)
show_info("张三", height=180)
show_info("张三")
show_info(age=21, name="张三", height=166)

print("abc", "123", 324, 46545)
print("哈哈")