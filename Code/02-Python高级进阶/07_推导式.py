"""
计算20以内所有偶数的平方和
"""

sum_num = 0
for i in range(1, 21): #（循环）
    # 判断是否是偶数 （过滤）
    if i % 2 == 0:
        sum_num += (i ** 2) # （处理）
        
print(sum_num)