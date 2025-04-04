"""
a = int(input("输入变量a: ")) # 不能传字符串，否则报错ValueError
b = int(input("输入变量b: "))
# 输出相加结果
print(a + b)
"""

"""
超市买苹果计算金额
需求:	
●  收银员输入苹果的价格price，单位：元/斤
●  收银员输入用户购买苹果的重量weight，单位：斤
●   计算并输出付款金额:xxx元
"""
price = float(input("苹果价格（元/斤）："))
weight = int(input("苹果重量（斤）："))

ss = "付款金额: %.2f 元" % (price * weight) # python2.0的写法
print(ss)