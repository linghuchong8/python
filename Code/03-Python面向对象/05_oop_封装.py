"""
需求
定义一个洗衣机类，其中包含了打开/关闭洗衣机门、设置洗衣模式、设置马达转速、开始洗衣服等方法。
在初始化时，需要传入品牌brand和容量capacity两个参数。洗衣机门的状态is_closed、洗衣模式__mode和马达转速motor_speed都有默认值。
调用wash()方法时，会根据门的状态和模式来执行相应的操作，最终完成洗衣任务。

步骤：
1. 定义WashMachine类，初始化时传入品牌和容量两个参数，并设置默认值。
2. 定义打开/关闭洗衣机门的方法，通过修改is_closed属性来实现。
3. 定义设置洗衣模式的方法，通过修改__mode属性来实现。
4. 定义设置马达转速的私有方法，通过修改motor_speed属性来实现。
5. 定义开始洗衣服的方法，根据门的状态和模式来执行相应的操作，最终完成洗衣任务。

6. 实例化WashMachine类，传入品牌和容量两个参数，得到一个洗衣机对象。
7. 调用打开/关闭洗衣机门的方法，模拟打开/关闭洗衣机门的操作。
8. 调用设置洗衣模式的方法，传入一个参数，设置洗衣模式。
9. 调用开始洗衣服的方法，根据门的状态和模式来执行相应的操作，最终完成洗衣任务。
"""
# 1. 定义WashMachine类，初始化时传入品牌和容量两个参数，并设置默认值。
class WashMachine:

    def __init__(self, brand, capacity) -> None:
        """
        初始化方法：品牌brand和容量capacity
        """   
        self.brand = brand
        self.capacity = capacity
        # 门是否关闭
        self.is_closed = True
        # 洗衣模式. #0默认 1轻柔 2狂揉
        self.__mode = 0
        # 马达速度
        self.__motor_speed = 0

    # 2. 定义打开/关闭洗衣机门的方法，通过修改is_closed属性来实现。
    def open_door(self):
        self.is_closed = False
        
    def close_door(self):
        self.is_closed = True
        
    # 3. 定义设置洗衣模式的方法，通过修改__mode属性来实现。
    def set_mode(self, new_mode):
        """调节洗衣模式
        :param new_mode: 模式 0默认 1轻柔 2狂揉
        :return: 1设置成功 0设置失败
        """
        if new_mode in [0, 1, 2]:
            self.__mode = new_mode
            return 1
        else:
            print("模式设置错误", new_mode)
            return 0
        
    # 4. 定义设置马达转速的私有方法，通过修改motor_speed属性来实现。
    def __set_motor_speed(self, speed):
        # -10, 2000000
        if speed < 0:
            speed = 0
        elif speed > 10000:
            speed = 10000
        
        self.__motor_speed = speed
    
    # 5. 定义开始洗衣服的方法，根据门的状态和模式来执行相应的操作，最终完成洗衣任务。
    def wash(self):
        # 检查洗衣机门状态，没关，提示
        if not self.is_closed:
            print("请关闭洗衣机门，哔哔哔哔！")
            return
        
        # 检查是否设置模式
        if self.__mode == 0:
            print("请先设置模式")
            return
        
        # 根据模式，设置不同的电机转速
        print("放水...")
        print("放满了...")
        if self.__mode == 1: # 轻柔模式
            # 调节马达转速 1000
            self.__set_motor_speed(1000)
            print("轻柔模式，洗内衣👙，马达转速：", self.__motor_speed)
        elif self.__mode == 2: # 狂柔模式
            # 调节马达转速 3000
            self.__set_motor_speed(3000)
            print("狂柔模式，洗大衣🧥，马达转速：", self.__motor_speed)
        
        print(self.brand, "开始洗衣服")
        print(self.brand, "洗完了，哔哔")
    

# 6. 实例化WashMachine类，传入品牌和容量两个参数，得到一个洗衣机对象。
machine = WashMachine("海尔", 10)
# 7. 调用打开/关闭洗衣机门的方法，模拟打开/关闭洗衣机门的操作。
machine.open_door()
machine.close_door()
# 8. 调用设置洗衣模式的方法，传入一个参数，设置洗衣模式。
machine.set_mode(2) #0默认 1轻柔 2狂揉
# 9. 调用开始洗衣服的方法，根据门的状态和模式来执行相应的操作，最终完成洗衣任务。
machine.wash()

print("----------------------------")

# 6. 实例化WashMachine类，传入品牌和容量两个参数，得到一个洗衣机对象。
小天鹅洗衣机 = WashMachine("小天鹅", 8)
# 7. 调用打开/关闭洗衣机门的方法，模拟打开/关闭洗衣机门的操作。
小天鹅洗衣机.open_door()
小天鹅洗衣机.close_door()
# 8. 调用设置洗衣模式的方法，传入一个参数，设置洗衣模式。
小天鹅洗衣机.set_mode(2) #0默认 1轻柔 2狂揉
# 9. 调用开始洗衣服的方法，根据门的状态和模式来执行相应的操作，最终完成洗衣任务。
小天鹅洗衣机.wash()
