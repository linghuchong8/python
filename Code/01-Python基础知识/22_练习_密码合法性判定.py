"""
判断登录密码是否合法。 
1. 密码必须是数字、字母(大小写都可以)、和下划线，否则不合法
2. 如果密码合法,就输出"密码合法"

合法： abc123
合法： BCD_123
不合法：hhew23@^83dW_fkf&E

分析
1. 定义容器，保存所有的数字 字母 _
2. for循环遍历密码中每一个元素
3. 判断每一个元素是否合法
4. 如果不合法，执行break
"""
password = input("请输入密码：")

# 1. 定义容器，保存所有的数字 字母 _
container = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
# 2. for循环遍历密码中每一个元素
for ele in password:
    # 3. 判断每一个元素是否合法
    if ele not in container:
        print("密码不合法，包含非法字符：", ele)
        break
else:
    print("密码合法：", password)