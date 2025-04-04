def milk_tea_shop(kind, *args, **kwargs):
    print(f"--- 老板：给我来一杯：{kind}!")
    print(f"--- 对不起，我们的{kind}卖完啦！ ")
    print("要求:", end=" ")
    for arg in args:
        print(arg, end=", ")
    print()
        
    print("----------------------")
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")

milk_tea_shop(
    "卡布奇诺珍珠奶茶",
    "走冰", "飞糖", "加珍珠",
    addr="创维创新谷2#B栋5楼", name="张生", phone="13688889999"
)