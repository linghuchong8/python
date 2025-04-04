"""
推导式指的是轻量级循环创建数据的方式，
对列表或可迭代对象中的每个元素应用某种操作，
用生成的结果创建新的列表；或用满足特定条件的元素创建子序列。

推导式包括：
● 列表推导式
● 元组推导式
● 集合推导式
● 字典推导式

列表推导式的格式：[计算公式 for循环 if判断]
"""
# 列表推导式
lst = [ele for ele in range(21)]
lst = [ele for ele in range(21) if ele % 2 == 0]
lst = [ele ** 2 for ele in range(21) if ele % 2 == 0]
print(lst, "sum -> ", sum(lst))

# 元组推导式
tup = (ele for ele in range(10))
print(tuple(tup), type(tup))

# 集合推导式
ss = {ele for ele in range(10)}
print(set(ss), type(ss))

# 字典推导式
dd = {key : key*2 for key in range(10)}
print(dd, type(dd))

names = ["zhangsan", "lisi", "wangwu"]
score = [33, 44, 55]
# print(list(zip(names, score)))

dd = {k:v for k, v in zip(names, score)}
print(dd)