name_list = ["柯南", "路飞", "卡卡西", "纲手", "流川枫"]
name = "haha"

# 查询
print(name_list[2])
# 获取指定元素的位置（索引)
print(name_list.index("纲手"))

# 追加
name_list.append("鸣人")
name_list.append("小樱")
name_list.append("雏田")
print(name_list)

# 移除指定元素（内容，索引）
name_list.remove("小樱")
print(name_list)
print(name_list.pop(4))
# 移除卡卡西: 索引2 (python2.0+)
del name_list[2]
print(name_list)

# 修改元素
name_list[0] = "工藤新一"
print(name_list)

# 排序 （原数组会被修改）
digit_list = [2, 4, 1, 23, 8, 2, 54, 12]
# digit_list.sort()             # 正序：从小到大
digit_list.sort(reverse=True)   # 倒序：从大到小
print(digit_list)

# 反转数组
digit_list2 = [2, 4, 1, 23, 8, 2, 54, 12]
digit_list2.reverse()
print(digit_list2)

print("----------------------------------")

students = [
    ["张飒", "李四", "王二麻子"],
    ["刘能", "王大拿"]
]
print(students[0][2])
print(students[1][0])
print(students[1][4]) # IndexError: list index out of range