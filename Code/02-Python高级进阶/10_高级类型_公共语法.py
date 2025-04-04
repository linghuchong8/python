"""
字符串，列表，元组
"""

arr = [1, 7, 3, 2, 7, 8, -3]

print("数组长度: ", len(arr))
print("数组求和：", sum(arr))

print("最大数:", max(arr))
print("最小数:", min(arr))

arr2 = ["a", "z", "c"]
print("x" in arr2)
print("y" in arr2)

print(arr + arr2)
print(arr2 * 3)

arr3 = ["a", "b", "k"]

print(arr2 == arr3)


t = (1,2,3)
print(t * 3)