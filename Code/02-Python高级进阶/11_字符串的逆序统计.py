"""
需求

完成字符串的逆序以及统计
设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
打印如下内容:
--------------------------------------------
您输入的字符串: zhongshanshan
长度: 13
逆序后为: nahsnahsgnohz
字符统计结果: z:1 h:3 o:1 n:3 g:1 s:2 a:2
--------------------------------------------
"""
string = ""

while True:
    string = input("请输入字符串：")
    if len(string) < 31:
        break
    
    print("您输入的字符串过长（超过30），请重新输入！")
    

sss = """--------------------------------------------
您输入的字符串: {}
长度: {}
逆序后为: {}
字符统计结果: {}
--------------------------------------------
"""

# print("success: ", string)
# 用字典记录每个字母出现的次数 dict()
stat_dict = {}
for char in string:
    # 如果字典里不存在当前字母
    if char not in stat_dict:
        stat_dict[char] = 1
    else:
        # 已经存在
        stat_dict[char] += 1

result = ["{}:{}".format(k, v) for k, v in stat_dict.items()]
# join将以上列表内容，用空格分割，合并成一个完整的字符串
# print(" ".join(result))

print(sss.format(
    string,
    len(string),
    string[::-1],
    " ".join(result)
))