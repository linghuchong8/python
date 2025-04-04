print(list(range(0, 10)))
print(list(range(2, 5)))
print(list(range(6)))

# 1个参数：[0, stop)
# 2个参数：[start, stop)
# 3个参数：start开始, stop结束, step步长(默认1)
#         [start, stop)
print(list(range(1, 10, 2)))

print(list(range(10, 2, -1)))

print("-------------------------------")
# range是个可迭代对象 
for i in range(10):
    print(i, end=", ")
    
print()

for i in range(10, 2, -1):
    print(i, end=", ")