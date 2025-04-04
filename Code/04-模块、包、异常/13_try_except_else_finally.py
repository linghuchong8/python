def write_file():
    # 以可写的方式，打开a.txt
    f = open('a.txt','w')
    try:
        # 写数据
        f.write('Good')
        # 出现异常
        a = 10
        b = 2
        re = a/b
    except:
        print('出现异常❗')
    else:
        print("未出现异常✅")
    finally: # 即使程序出现异常  finally里面的代码也可以继续执行
        # 必须要关闭 内存泄漏
        f.close()
        print('文件已经关闭了')
        
# print(read_file(10, 0))
write_file()