"""
1
12
123
1234
12345
"""
row = 1
# 遍历所有行
while row <= 5:
    # 打印每行的所有内容
    col = 1
    while col <= row:
        print(col, end="")    
        col += 1
        
    # 换行
    print()
    
    row += 1