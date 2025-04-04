"""需求:
●  在控制台依次提示用户输入:姓名name、公司com、职位title、电话telephone、邮箱email
●  按照指定格式输出
offer
"""
name    = input("姓名：")
company = input("公司：")
title   = input("职位：")
phone   = input("电话：")
email   = input("邮箱：")

print("*" * 50)
print(company)
print()
# print("%s（%s）" % (name, title))
print("{}（{}）".format(name, title))
print()
print("电话：", phone)
print("邮箱：", email)

print("*" * 50)
