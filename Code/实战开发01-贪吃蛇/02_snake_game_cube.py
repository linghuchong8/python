"""
贪吃蛇开发：

1. 把蛇身和食物绘制出来（优化）
2. 能让蛇身动起来（上下左右）
    a. 将蛇头复制一份
    b. 复制的蛇头向当前方向移动一格
    c. 把新的蛇头插入到头部
    d. 删除蛇尾即可
3. 根据用户键盘输入修改运动方向
4. 碰撞判断：蛇头与食物
    a. 蛇身长一节
    b. 食物随机生成到新的位置
5. 碰撞判断：蛇头与墙体/身体
    a. 蛇头碰到墙体
    b. 蛇头碰到身体
6. 实时分数和FPS(Frame Per second)显示
7. 结束提示：得分，按键重新开始

"""
from game import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

BLOCK_SIZE  = 20

MOVE_DICT = {
    0: ( 1,  0),   # 右
    1: ( 0,  1),   # 下
    2: (-1,  0),   # 左
    3: ( 0, -1)    # 上
}

class Snake:
    
    def __init__(self) -> None:
        # 蛇运动的方向 右0，下1，左2，上3
        self.direction = 0 
        self.snake_body = [
            [6 * BLOCK_SIZE, 3 * BLOCK_SIZE],
            [5 * BLOCK_SIZE, 3 * BLOCK_SIZE],
            [4 * BLOCK_SIZE, 3 * BLOCK_SIZE],
            [4 * BLOCK_SIZE, 2 * BLOCK_SIZE],
        ]
    
    def draw(self, qp: QPainter):
        """绘制蛇头和蛇身
        :param qp: 画笔
        """
        # 绘制蛇身
        # 设置笔刷颜色
        qp.setBrush(COLOR_BLUE)
        for x, y in self.snake_body[1:]:
            # 绘制矩形x,y,w,h
            qp.drawRect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            
        # 绘制蛇头
        head_x, head_y = self.snake_body[0]
        # 设置笔刷颜色
        qp.setBrush(COLOR_GREEN)
        # 绘制矩形x,y,w,h
        qp.drawRect(head_x, head_y, BLOCK_SIZE, BLOCK_SIZE)
        
    
    def move(self):
        """
        2. 能让蛇身动起来（上下左右）
            a. 将蛇头复制一份
            b. 将复制的蛇头向当前方向移动一格
            c. 把新的蛇头插入到头部
            d. 删除蛇尾即可
        """
        # a. 将蛇头复制一份
        new_head = self.snake_body[0][:]
        new_move = MOVE_DICT[self.direction]
        
        # b. 将复制的蛇头向当前方向移动一格
        new_head[0] += new_move[0] * BLOCK_SIZE
        new_head[1] += new_move[1] * BLOCK_SIZE
        
        # c. 把新的蛇头插入到头部
        self.snake_body.insert(0, new_head)
        
        # d. 删除蛇尾即可
        self.snake_body.pop()
        
    def grow(self):
        """蛇身生长"""
        # 取出尾巴坐标，复制一份
        new_tail = self.snake_body[-1][:]
        # 插入到尾部
        self.snake_body.append(new_tail)
        
    
class Food:
    
    def __init__(self, x, y) -> None:
        """
        640x480
        640/20 = 32 x:[0, 31]
        480/20 = 24 y:[0, 23]
        """
        self.node = [x, y]
    
    def draw(self, qp: QPainter):
        x, y = self.node
        # 设置笔刷颜色
        qp.setBrush(COLOR_RED)
        # 绘制矩形x,y,w,h
        qp.drawRect(x , y , BLOCK_SIZE, BLOCK_SIZE)

class SnakeGame(Game):
    
    def __init__(self):
        super().__init__()
        # 设置标题
        self.setWindowTitle("贪吃蛇游戏")
        # 设置窗口尺寸, 并禁止拖拽修改窗口尺寸
        self.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        # 设置窗口图标
        self.setWindowIcon(QIcon("img/icon.png"))
        
        # 构建所有地图网格点的数组 
        # [0,0] [20, 0] [40, 0] ... [620, 0]
        # [0,20] [20, 20] [40, 20] .... [620, 20]
        self.map_points = []
        # x: [0, 640)  y: [0, 320)
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
                self.map_points.append([x, y])
        
        # print(self.map_points)
        self.set_fps(8)
        
        
    def keyPressEvent(self, event: QKeyEvent):
        """处理按键事件
        哪个按键，按下抬起
        """
        super().keyPressEvent(event)
        key = event.key()
        if key == Qt.Key_Left:
            print("左")
            self.snake.direction = 2
        elif key == Qt.Key_Right:
            print("右")
            self.snake.direction = 0
        elif key == Qt.Key_Up:
            print("上")
            self.snake.direction = 3
        elif key == Qt.Key_Down:
            print("下")
            self.snake.direction = 1
        
    def generate_new_food(self):
        # 生成新的食物坐标
        # 通过推导式，过滤掉蛇的部分，得到新的数组
        new_map = [node for node in self.map_points if node not in self.snake.snake_body]
        
        # 蛇身占据了所有地图
        if len(new_map) == 0: return
        
        # 生成新的坐标, 随机从列表取元素
        new_node = random.choice(new_map)
        print("new_node:", new_node)
        self.food = Food(new_node[0], new_node[1])
        
        
    def on_time_event(self, event):
        """处理每帧时间事件
        """
        # 进行移动（修改数值）
        self.snake.move()
        # 进行碰撞判断
        # 4. 碰撞判断：蛇头与食物
        snake_head = self.snake.snake_body[0]
        if snake_head == self.food.node:
            print("碰到食物")
            # a. 蛇身长一节
            self.snake.grow()
            # b. 食物随机生成到新的位置
            # self.food = Food(20 * BLOCK_SIZE, 15 * BLOCK_SIZE)
            self.generate_new_food()
            
        # 5. 碰撞判断：蛇头与墙体/身体
        head_x, head_y = snake_head
        # a. 蛇头碰到墙体
        if head_x >= SCREEN_WIDTH or head_x < 0:
            print("碰到左右墙体")
            self.is_game_over = True
        elif head_y >= SCREEN_HEIGHT or head_y < 0:
            print("碰到上下墙体")
            self.is_game_over = True
        
        # b. 蛇头碰到身体 (蛇头坐标==蛇身任意坐标)
        if snake_head in self.snake.snake_body[1:]:
            print("碰到自己")
            self.is_game_over = True
            
        
    def draw_content(self, qp: QPainter):
        """绘制界面内容
        :param qp: 画笔
        """
        # -----------------------------------------绘制蛇头&蛇身
        self.snake.draw(qp)
        # -----------------------------------------绘制食物
        self.food.draw(qp)
        
    def start_game(self):
        """游戏开始前的初始化
        """
        self.snake = Snake()
        self.generate_new_food()
        
        super().start_game()
    

if __name__ == '__main__':
    SnakeGame.start()