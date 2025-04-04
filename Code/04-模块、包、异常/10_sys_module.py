import sys

print(sys.argv) # 脚本的执行参数
print(sys.argv[1:])
print(sys.path) # 依赖的包和模块所在路径
# sys.exit(0)

print("------------------------------------ time")
import time

# 时间戳，是从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数
start = time.time() 
# time.sleep(2) # 睡2秒
end   = time.time()
print(end, end - start)

print("----------------------------------- datetime") # 上位机
from datetime import datetime
# 获取当前的日期时间
now = datetime.now()
print(now, type(now))
print(now.year, now.month, now.day)
# 将datetime对象生成指定格式的字符串 2024年05月03日 09:13:14
str_time = datetime.strftime(now, "%Y年%m月%d日 %H:%M:%S")
# 也可以将指定格式字符串解析成datetime对象 
cur_time = datetime.strptime("2024年05月03日 09:13:14", "%Y年%m月%d日 %H:%M:%S")

print(str_time, type(str_time))
print(cur_time, type(cur_time))

print("------------------------------------ sort")
aaa = [2, 4, 1, -2, 3, 6, 12, 8]
print(max(aaa))
print(min(aaa))
print(sum(aaa))
print(len(aaa))
# sorted生成新的数组，不修改原数组
print(sorted(aaa))
print(sorted(aaa, reverse=True))
print(aaa)

print("-------------------------------------- math")
import math
# 幂
print(math.pow(5, 3))
# 向上取整
print(math.ceil(1.2136594))
# 向下取整
print(math.floor(1.9136594))
# 四舍五入
print(round(1.2136594))
print(round(1.6136594))

# sin,cos. 30,45,60 -> π/6, π/4, π/3
print(math.pi)
print(math.sin(math.pi / 6)) # 弧度 (sin参数)

print("---------------------------------------- random")
import random

# 随机整数
print(random.randint(10, 20))
# 随机小数[0, 1) 
print(random.random())
# 随机浮点数（指定范围）
print(random.uniform(1.3, 3.4))

# 从列表中随机抽签
lst = ["张三", "李四", "王五", "赵六"]
print(random.choice(lst))
print(random.choices(lst))