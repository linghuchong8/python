a = 10
b = 0

try:
    print(a / b)
    print("正常执行代码✅")
except ZeroDivisionError as e:
    print("出现异常❌", e)
    
print("其他下方代码")