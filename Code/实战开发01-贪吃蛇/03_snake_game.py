"""
贪吃蛇开发：

✅1. 把蛇身和食物绘制出来（优化）    绘制
✅2. 能让蛇身动起来（上下左右）      按键
    a. 将蛇头复制一份
    b. 复制的蛇头向当前方向移动一格
    c. 把新的蛇头插入到头部
    d. 删除蛇尾即可
✅3. 根据用户键盘输入修改运动方向     按键
✅4. 碰撞判断：蛇头与食物            事件
    a. 蛇身长一节
    b. 食物随机生成到新的位置
✅5. 碰撞判断：蛇头与墙体/身体        事件
    a. 蛇头碰到墙体
    b. 蛇头碰到身体
✅6. 实时分数和FPS(Frame Per second)显示     绘制
✅7. 结束提示：得分，按键重新开始             绘制

- ✅添加背景图    
- ✅添加横纵网格
- ✅添加蛇头图片
- ✅蛇身变圆角矩形
- ✅蛇身不能掉头运动
- ✅蛇身穿墙功能

"""
from game import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

BLOCK_SIZE  = 20

# 移动方向字典
MOVE_DICT = {
    Qt.Key_Right : ( 1,  0),   # 右
    Qt.Key_Down  : ( 0,  1),   # 下
    Qt.Key_Left  : (-1,  0),   # 左
    Qt.Key_Up    : ( 0, -1)    # 上
}

# 蛇头角度字典
HEAD_ANGLE_DICT = {
    Qt.Key_Right : -90,    # 右
    Qt.Key_Down  :   0,    # 下
    Qt.Key_Left  :  90,    # 左
    Qt.Key_Up    : 180     # 上
}

class Snake:
    
    def __init__(self) -> None:
        # 蛇运动的方向 右0，下1，左2，上3
        self.direction = Qt.Key_Right 
        self.is_cross_wall = True
        self.snake_body = [
            [6 * BLOCK_SIZE, 3 * BLOCK_SIZE],
            [5 * BLOCK_SIZE, 3 * BLOCK_SIZE],
            [4 * BLOCK_SIZE, 3 * BLOCK_SIZE],
            [4 * BLOCK_SIZE, 2 * BLOCK_SIZE],
        ]
        self.head_img = QImage("img/head-red.png")
        # 修改图片尺寸
        self.head_img = self.head_img.scaled(BLOCK_SIZE, BLOCK_SIZE)
        # 分数
        self.score = 0
    
    def draw(self, qp: QPainter):
        """绘制蛇头和蛇身
        :param qp: 画笔
        """
        # 绘制蛇身
        # 设置画笔边缘为透明色
        # qp.setPen(QPen(Qt.transparent))
        qp.setPen(QColor(255, 255, 255, 0))
        # 设置笔刷颜色
        qp.setBrush(COLOR_BLUE)
        for x, y in self.snake_body[1:]:
            # 圆角矩形
            qp.drawRoundedRect(x, y, BLOCK_SIZE, BLOCK_SIZE, 5, 5)
            
        # 绘制蛇头
        head_x, head_y = self.snake_body[0]
        # 根据方向旋转蛇头图片
        angle = HEAD_ANGLE_DICT[self.direction]
        new_img = self.head_img.transformed(QTransform().rotate(angle))
        # 绘制图片
        qp.drawImage(head_x, head_y, new_img)
    
    def change_direction(self, event: QKeyEvent):
        """根据用户按键，修改蛇运动方向
        左右运动：修改为上下
        上下运动：修改为左右
        """
        key = event.key()
        LR = [Qt.Key_Left, Qt.Key_Right]
        UD = [Qt.Key_Up, Qt.Key_Down]
        if key not in (LR + UD):
            print("非法操作", key)
            return
        
        if key == Qt.Key_Left:
            print("⬅️")
        elif key == Qt.Key_Right:
            print("➡️")
        elif key == Qt.Key_Up:
            print("⬆️")
        elif key == Qt.Key_Down:
            print("⬇️")
            
        # 左右运动：只能修改为上下
        if key in LR and self.direction in LR:
            return
        # 上下运动：只能修改为左右
        if key in UD and self.direction in UD:
            return
        
        # 进行修改    
        self.direction = key
    
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
        
        # 如果新的头部坐标超出屏幕范围，则从屏幕的另一端出现（需要开启）
        if self.is_cross_wall:
            if new_head[0] >= SCREEN_WIDTH:
                new_head[0] = 0
            elif new_head[0] < 0:
                new_head[0] = SCREEN_WIDTH - BLOCK_SIZE
            
            if new_head[1] >= SCREEN_HEIGHT:
                new_head[1] = 0
            elif new_head[1] < 0:
                new_head[1] = SCREEN_HEIGHT - BLOCK_SIZE
        
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
        # 分数加1
        self.score += 1
        
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
        
        self.snake : Snake = None
        self.food : Food = None
        
        # 加载bg.png作为背景图
        self.background_img = QImage("img/bg.png")
        # 缩放图片
        self.background_img = self.background_img.scaled(SCREEN_WIDTH, SCREEN_HEIGHT)
        
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
        
        if self.snake is not None:
            self.snake.change_direction(event)
        
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
        # ----------------------------- 进行移动（修改数值）
        self.snake.move()
        # 进行碰撞判断
        # 4. --------------------------- 碰撞判断：蛇头与食物
        snake_head = self.snake.snake_body[0]
        if snake_head == self.food.node:
            print("碰到食物")
            # a. 蛇身长一节
            self.snake.grow()
            # b. 食物随机生成到新的位置
            # self.food = Food(20 * BLOCK_SIZE, 15 * BLOCK_SIZE)
            self.generate_new_food()
            
        # 5. ---------------------------碰撞判断：蛇头与墙体/身体
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
            
    def draw_text(self, qp: QPainter):
        # 6. 实时分数和FPS(Frame Per second)显示
        # 左上角绘制白色的文字： score: 分数
        # 设置字体
        qp.setFont(QFont("Arial", 18))
        # 设置画笔颜色
        qp.setPen(COLOR_WHITE)
        # 绘制文字
        qp.drawText(20, 30, "score: " + str(self.snake.score))
        # 右上角绘制白色的文字： fps: xxx
        # 绘制文字
        qp.drawText(SCREEN_WIDTH - 100, 30, "fps: " + str(self.fps))
    
        # 7. 结束提示：得分，按键重新开始
        if self.is_game_over:
            # 设置画笔颜色
            qp.setPen(COLOR_WHITE)
            # 设置加粗24号字体
            qp.setFont(QFont("Microsoft YaHei", 24, weight=QFont.Bold))
            # 绘制文字
            qp.drawText(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50, "游戏结束")
            # 设置18号字体
            qp.setFont(QFont("Microsoft YaHei", 18))
            # 绘制文字
            qp.drawText(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 50, "Score: " + str(self.snake.score))
            # 绘制文字
            qp.drawText(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 100, "Press space to restart")
            
    def draw_content(self, qp: QPainter):
        """绘制界面内容
        :param qp: 画笔
        """
        # 画笔设置抗锯齿
        qp.setRenderHint(QPainter.Antialiasing)
        
        # ---------------------------------------- 添加背景图
        qp.drawImage(0, 0, self.background_img)
        # ---------------------------------------- 添加横纵网格
        # 画笔颜色设置为灰色
        qp.setPen(COLOR_GRAY)
        # 画所有的横线， 间隔为BLOCK_SIZE
        # [0, 0]  -> [640, 0], 
        # [0, 20] -> [640, 20]
        # ...
        # [0, 460] -> [640, 460]
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE): # y: [0, 480)
            qp.drawLine(0, y, SCREEN_WIDTH, y)
        # 画所有的竖线， 间隔为BLOCK_SIZE
        # [0, 0]  -> [0, 480], 
        # [20, 0] -> [20, 480]
        # ...
        # [620, 0] -> [620, 480]
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE): # x: [0, 640)
            qp.drawLine(x, 0, x, SCREEN_HEIGHT)
        
        # -----------------------------------------绘制蛇头&蛇身
        self.snake.draw(qp)
        # -----------------------------------------绘制食物
        self.food.draw(qp)
        # ---------------------------------------- 实时分数和FPS显示
        self.draw_text(qp)
        
    def start_game(self):
        """游戏开始前的初始化
        """
        self.snake = Snake()
        self.generate_new_food()
        
        super().start_game()
    

if __name__ == '__main__':
    SnakeGame.start()