a = 5
b = 2
print("---------------------------------- 赋值运算符")
a += b
print(a) # 7

a /= b
print(a) # 3.5

a //= b
print(a) # 1.0

a = 5
b = 2
a *= 2
print(a) # 10

a **= 2
print(a) # 100

a += 1
a %= 2
print(a) # 1

print("-------------------------------- 比较运算符")
a = 5
b = 2
print(a <= b) # False
print(a == b) # False
print(a != b) # True
print(a >= b) # True

print("--------------------------------- 逻辑运算符 and or")
print("严格要求 与：", True and True)   # False
print("心态良好 或：", True or  False)  # True
print("对向取反 非：", not True)        # False



