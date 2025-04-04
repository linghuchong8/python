"""
1. 创建 家具对象, 输出 家具信息
2. 创建 房子对象, 输出 房子信息
3. 房子添加家具, 输出 房子信息
"""
class Item:
    """家具类
    """

    def __init__(self, name, area):
        """初始化家具的方法
        :param name: 家具名称
        :param area: 家具占地面积
        """
        self.name = name
        self.area = area

    def __str__(self) -> str:
        return "str家具: {}, 占地面积: {}".format(self.name, self.area)
    
    def __repr__(self) -> str:
        return "repr家具: {}, 占地面积: {}".format(self.name, self.area)


class House:
    """房子类
    """
    def __init__(self, address, area):
        """房子的初始化方法
        :param address: 地址
        :param area: 房子面积
        """
        self.address = address
        self.area = area
        # 剩余面积，会随着家具的添加而减少
        self.free_area = area 
        # 家具列表
        self.items = []
    
    def add_item(self, item: Item):
        """给房子添加家具，条件：房屋剩余面积>=家具占地面积
        :param item: 家具
        """
        if self.free_area >= item.area:
            # 把家具添加到列表
            self.items.append(item)
            # 修改剩余面积
            self.free_area -= item.area
            # 可以添加
            print("添加家具【{}】成功".format(item.name))        
            return 1
        else:
            print("添加【{}】失败，房屋剩余面积不足".format(item.name))
            return 0
            
    def __str__(self) -> str:
        return "房子地址：{}, 面积：{}, 剩余：{}".format(self.address, self.area, self.free_area)
    
# 创建家具
item1 = Item("沙发床", 40)
item2 = Item("桌椅", 10)
item3 = Item("家庭影院", 70)

print(item1)
print(item2)
print(item2)

# 创建房子
house = House("深圳湾一号3栋304", 100)
print(house)
print("-------------------------------------------")

# 给房子添加家具
house.add_item(item1)
house.add_item(item2)
house.add_item(item3)

print(house)
# 打印房子里所有的家具(如果打印一个包含多个对象的容器，需要重写__repr__)
print("所有家具：", house.items)