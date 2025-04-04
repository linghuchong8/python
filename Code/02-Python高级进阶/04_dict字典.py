ages = {
    "Tom": 18,
    "Jack": 20,
    "Alex": 17
}
print(ages)
print("--------------------------------- 增删改查")

# 添加
ages["张三"] = 33
ages.setdefault("李四", 44)

# 删除
ages.pop("Alex")
# del ages["Alex"]

# 修改
ages["Jack"] = 23

# 查询
print(ages["Tom"])


# 先判断是否存在，再取值
if "Tom" in ages:
    print("Tom age: ", ages["Tom"])
    
# 清空字典
ages.clear()

print(ages) 