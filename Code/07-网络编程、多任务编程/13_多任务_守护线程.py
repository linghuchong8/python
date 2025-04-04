import time
import threading

def singing():
    print("singing线程：", threading.currentThread())
    for i in range(10):
        print("唱歌🎤...", i)
        time.sleep(0.5)

def dancing():
    print("dancing线程：", threading.currentThread())
    for i in range(10):
        print("跳舞💃...", i)
        time.sleep(0.5)
        
if __name__ == '__main__':
    print("主线程", threading.currentThread())
    # 创建子线程
    t1 = threading.Thread(target=singing)
    t2 = threading.Thread(target=dancing, daemon=True)
    # 将子线程设置为守护线程(所有子线程都需要同时daemon，才能生效)
    t1.daemon = True
    t1.start()
    t2.start()
    
    # 不能在start之后设置守护状态。cannot set daemon status of active thread
    # t1.daemon = True
    
    # 主线程在2s后主动退出
    time.sleep(2)
    print("主线程执行完毕，退出")
    exit(-3)