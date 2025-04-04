import time
import threading

def singing():
    print("singing线程：", threading.currentThread())
    for i in range(5):
        print("唱歌🎤...", i)
        time.sleep(0.5)

def dancing():
    print("dancing线程：", threading.currentThread())
    for i in range(5):
        print("跳舞💃...", i)
        time.sleep(0.5)
        
if __name__ == '__main__':
    print("主线程", threading.currentThread())
    # 创建子线程
    t1 = threading.Thread(target=singing)
    t2 = threading.Thread(target=dancing)
    t1.start()
    t2.start()
