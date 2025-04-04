ss = {"孙悟空", "白骨精", "唐僧", "猪八戒", "孙悟空", "沙和尚"}  
print(ss)

for item in ss:
    print(item)
    
print("-----------------------")
ss.add("沙悟净")

# 如果集合不包含要移除的元素，报错KeyError
# ss.remove("沙师弟")
# 丢弃元素，不存在也不报错
ss.discard("沙和尚")

# 随机移除一个
print(ss.pop())

# 清除全部
# ss.clear()

print(ss)