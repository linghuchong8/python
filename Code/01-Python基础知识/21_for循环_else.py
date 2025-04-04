for i in range(10):
    if i == 3:
        break
    print("媳妇，我错了", i)
else:
    print("顺利完成！")
    
print("--------------------")

for i in range(10):
    if i % 2 != 0:
        continue
    print("媳妇，我错了", i)
else:
    print("顺利完成！")