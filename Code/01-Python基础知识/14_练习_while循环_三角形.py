# 根据用户输入的数值n，打印n行*三角形

n = int(input("请输入数字N: "))

# 正三角形
row = 1
while row <= n:
    print("*" * row)
    row += 1
    
print("------------------------------")
    
# 倒三角形
row = n
while row >= 1:
    print("*" * row)
    row -= 1