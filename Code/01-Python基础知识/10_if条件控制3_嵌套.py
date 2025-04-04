"""
需求：
1. 定义布尔型变量 has_ticket 表示是否有车票
2. 定义整型变量 knife_length 表示刀的长度，单位：厘米
3. 首先检查是否有车票，如果有，才允许进行 安检
4. 安检时，需要检查刀的长度，
5. 判断是否超过 20 厘米
  a. 如果不超过 20 厘米，安检通过
  b. 如果超过 20 厘米，提示刀的长度，不允许上车
6. 如果没有车票，不允许进门
"""
rst = eval("4 + 3 * 7")
print("rst: ", rst, type(rst))
rst = eval("True")
print("rst: ", rst, type(rst))

has_ticket = eval(input("是否有车票："))  # 1, 0 evalution
knife_length = int(input("带刀的长度："))

if has_ticket:
    print("有票：", has_ticket)
    if knife_length <= 20:
        print("可以上车，刀长：", knife_length)
    else:
        print("不准上车，刀太长：", knife_length)
else:
    print("没票，不准上车")
