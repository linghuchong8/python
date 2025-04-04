"""
1. 遍历所有的三位数
2. 求 百位 十位个位  立方和
3. 判断并打印
"""

# 153
for i in range(100, 1000):
    # 取出个位，十位，百位
    baiwei  = i // 100
    shiwei  = i // 10 % 10
    gewei   = i % 10
    # 计算所有数的立方和
    if (baiwei ** 3 + shiwei ** 3 + gewei ** 3) == i:
        print("水仙花数：{}+{}+{}={}".format(baiwei ** 3, shiwei ** 3, gewei ** 3, i))