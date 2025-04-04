names = ("柯南", "毛利")
print(type(names))

# 如果声明tuple的时候, 只有一个元素，必须在末尾加上逗号,以示区分
names = ("柯南",)
print(type(names))

print("------------------------------------ 自动组包解包")

names = "柯南", 666, "佐助"
print(type(names))

# 组包
stu = "柯南道尔", 23, 172.3
# 解包
name, age, height = stu
print("name:{} age:{} height:{}".format(name, age, height))

print("------------------------------------- 数据交换")
a = 4
b = 7

temp = a
a = b
b = temp
print(a, b)

a = 2
b = 3
b, a = a, b
print(a, b)

print("------------------------------------- 将list改为不可修改的tuple")
name_list = ["柯南", "路飞", "卡卡西", "纲手", "路飞","流川枫"]
name_list = tuple(name_list)
# name_list[2] = "旗木"
print(name_list.count("路飞"))