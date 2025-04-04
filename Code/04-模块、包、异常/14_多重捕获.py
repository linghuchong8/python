try:
    # 除零异常
    a , b = 10, 3
    c = a / b
    # 索引越界异常
    arr = [1,2,3,4]
    rst = arr[10]       # IndexError: list index out of range
except ZeroDivisionError as e:
    print("分母不能为0", e)
except IndexError as e:
    print("列表索引越界", e)
    
