""" 黑马名片管理系统

1. 程序启动，显示名片管理系统欢迎界面，并显示功能菜单
2. 用户用数字选择不同的功能：新建名片、显示名片、查询名片、退出系统
  a. 用户名片需要记录用户的 姓名、电话、QQ、邮件
  b. 显示名片可以列举出所有已经保存的名片
  c. 如果查询到指定的名片，用户可以选择 修改、删除 名片
"""

main_menu = """**************************************************
欢迎使用[名片管理系统]V1.0

1. 新建名片
2. 显示名片
3. 查询名片

0. 退出系统
**************************************************
"""
# 姓名、电话、QQ、邮件
card_list = [
    ["张三", "13800138000", "123456", "zhangsan@163.com"],
    ["王五", "13800138002", "987654", "wangwu@163.com"],
    ["李四", "13800138001", "456789", "lisi@163.com"]
]

def show_all_card():
    print("【显示名片】")
    print("姓名\t电话\t\tQQ\t邮件")
    for card in card_list:
        # 把card变量拆开，分别赋值给name、phone、qq、email
        name, phone, qq, email = card
        print("{}\t{}\t{}\t{}".format(name, phone, qq, email))

def create_card():
    print("新建名片")
    # 输入姓名、电话、QQ、邮件
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ：")
    email = input("请输入邮箱：")
    # 保存到card_list列表中
    card_list.append([name, phone, qq, email])
    print("【{}】名片保存成功！".format(name))

def modify_card(card):
    # 输入姓名、电话、QQ、邮件
    card[0]  = input("请输入姓名：")
    card[1]  = input("请输入电话：")
    card[2]  = input("请输入QQ：")
    card[3]  = input("请输入邮箱：")
    

def handle_card(card):
    name, phone, qq, email = card
    print("{}\t{}\t{}\t{}".format(name, phone, qq, email))
    action = input("请输入对名片的操作: 1.修改 2.删除 其他:退出修改\n -> ")
    if action == "1":
        modify_card(card)
        print("修改成功: ", name)
    elif action == "2":
        card_list.remove(card)
        print("删除成功: ", name)
        
        
def search_card():
    """搜索指定名片
    1. 输入姓名
    2. 遍历card_list列表，找到姓名相同的名片
    3. 显示名片信息，并提供修改、删除、退出编辑功能
    """
    print("【查询名片】")
    input_name = input("请输入姓名：")
    for card in card_list:
        name = card[0]
        if name == input_name:
            # 找到了指定的名片
            print("找到【{}】的名片：".format(name))
            handle_card(card)
            break
    else:
        # 未找到指定的名片
        print("【{}】的名片不存在！".format(input_name))

while True:
    print(main_menu)
    action = input("请输入操作：")
    if action == "1":
        create_card()
    elif action == "2":
        show_all_card()
    elif action == "3":
        search_card()
    elif action == "0":
        print("退出系统")
        break
    else:
        print("输入错误【{}】，请重新输入！".format(action))