ss = "Hello"
print(ss[1])

print("---------------------------- 判断")
print("abCD".isalpha()) 
 
print("1232".isdecimal())
print("1232".isdigit())
print("一二123三②四".isnumeric()) # 支持特殊数字

print("abcdef".startswith("abc"))
print("abcdef".endswith("def"))

print("----------------------------- 查找")
print("abcdef".find("d"))
print("abcdef".find("x")) # 找不到，返回-1
print("www.itheima.com".rfind(".")) # 从右边开始找
print("wmww.mitheima.com".replace("m", "M", 2))

print("------------------------------ 切割")
print("poplar|13633334444|123456".split("|"))
print("poplar 1363333   4444    123456".split()) # 无参数情况下，按照空格切割

print("----------------------------- 去空白")
print("     abc \t\r\n   ".strip()) 