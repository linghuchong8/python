"""
需求：
1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
2. 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
3. 比较胜负并输出结果
"""
# 导入random模块
import random

# 石头（1）／剪刀（2）／布（3）
your = int(input("请出拳："))

# 电脑随机出拳
comp = random.randint(1, 3)

# 我赢，平局，电脑赢
if (your == 3 and comp == 1) or (your == 2 and comp == 3) or (your == 1 and comp == 2):
    print("You Win! your={} comp={}".format(your, comp))
elif your == comp:
    print("平局 Tie")
else:
    print("Computer Win! your={} comp={}".format(your, comp))