name = "pkg.hello"

def say():
    print("pkg.Hello World")
    
def mul(a, b):
    return a * b
    
class Nice():
    
    def __init__(self) -> None:
        self.name = "pkg.hello Nice"
        
# 情况1：当前文件（模块）直接运行时，__name__是__main__
# 情况2：当前文件作为模块被引用时，__name__文件名（模块名）
# print(">>>", __name__, "<<<")

if __name__ == '__main__':
    print("执行一些测试代码")

    if mul(3, 7) == 21:
        print("测试成功")
