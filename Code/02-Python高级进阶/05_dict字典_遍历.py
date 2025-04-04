# key:value

ages = {
    "Tom": 18,
    "Jack": 20,
    "Alex": 17
}

# 遍历
for item in ages:
    print(item)

print("------------------------")    
# 遍历所有的key
for key in ages.keys():
    print(key, ages[key])

print("------------------------")    
# 遍历所有的value
for value in ages.values():
    print(value)
    
print("------------------------")    
# 遍历所有的键值对
for item in ages.items():
    print(item, type(item))

# 对每个键值对（元组）自动解包
for key, value in ages.items():
    print(key, value)
