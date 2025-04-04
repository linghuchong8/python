"""
99乘法表
"""
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("{} x {} = {}".format(col, row, col * row), end="\t")
        col += 1
    print()
    row += 1
    
print("-" * 100)

row = 9
while row >= 1:
    col = 1
    while col <= row:
        print("{} x {} = {}".format(col, row, col * row), end="\t")
        col += 1
    print()
    row -= 1