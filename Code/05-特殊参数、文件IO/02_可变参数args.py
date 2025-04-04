"""
元组可变参数
"""

def sum_nums(*args):
    print(type(args))
    # tuple
    print(args)
    # 拆开每个元素
    print(*args)
    print(1,2,3,4)
    
    rst = 0
    for arg in args:
        rst += arg
    return rst


def sum_nums1(name, *args):
    print(f"name:【{name}】")
    
    rst = 0
    for arg in args:
        rst += arg
    return rst

# a = sum_nums(1, 2, 3, 4)
a = sum_nums1("求和", 2, 3, 4)
print(a)