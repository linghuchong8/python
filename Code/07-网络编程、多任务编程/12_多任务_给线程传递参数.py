import time
import threading

def singing(name, age = 18, score=100):
    print("评分：", score)
    for i in range(5):
        print("{} [{}]唱歌🎤...{}".format(name, age, i))
        time.sleep(0.5)

if __name__ == '__main__':
    print("主线程", threading.currentThread())
    # 参数传递：
    # 方式1： 元组，只有一个元素时，需要添加逗号
    # t1 = threading.Thread(target=singing, args=("张韶涵",))
    
    # 方式2： 字典，不要求传参顺序
    # t1 = threading.Thread(target=singing, kwargs={ "score": 98, "name": "刘亦菲"})
    
    # 方式3： 组合 (元组和字典里的参数内容不能冲突)
    t1 = threading.Thread(target=singing, args=("张韶涵", ), kwargs={ "score": 98, "age": 22})
    t1.start()
