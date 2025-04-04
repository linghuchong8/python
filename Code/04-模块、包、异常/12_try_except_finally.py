def read_file(a, b):
    
    try:
        # 打开文件资源
        # 可能存在异常的操作
        rst = a / b
        print("没有异常时，执行的代码")
        return rst
    finally:
        # 关闭文件
        print("finally执行, 释放资源")
        
def write_file():
    # 以可写的方式，打开a.txt
    f = open('a.txt','w')
    try:
        # 写数据
        f.write('Good')
        # 出现异常
        a = 10
        b = 0
        re = a/b
    except:
        print('出现异常')
    finally: # 即使程序出现异常  finally里面的代码也可以继续执行
        # 必须要关闭 内存泄漏
        f.close()
        print('文件已经关闭了')
        
# print(read_file(10, 0))
write_file()