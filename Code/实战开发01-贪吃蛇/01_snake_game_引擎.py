"""
继承了Game的空类
"""
from game import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class SnakeGame(Game):
    
    def __init__(self):
        super().__init__()
        # 设置标题
        self.setWindowTitle("贪吃蛇游戏")
        # 设置窗口尺寸, 并禁止拖拽修改窗口尺寸
        self.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        # 设置窗口图标
        self.setWindowIcon(QIcon("img/icon.png"))
        
        self.x = 100
        self.y = 200
        self.width = 50
        self.height = 50
        
    def keyPressEvent(self, event: QKeyEvent):
        """处理按键事件
        """
        super().keyPressEvent(event)
        print("1. 处理用户按键&鼠标事件")
        
    def on_time_event(self, event):
        """处理每帧时间事件
        """
        print("2. 处理游戏里的每帧时间事件（游戏逻辑）")
        self.x += 10
        self.y += 10
        
    def draw_content(self, qp: QPainter):
        """绘制界面内容
        :param qp: 画笔
        """
        print("3. 绘制界面内容（每一帧）")
        qp.setBrush(COLOR_RED)
        qp.drawEllipse(self.x, self.y, self.width, self.height)
    
    def start_game(self):
        """游戏开始前的初始化
        """
        print("0. 游戏开始，初始化游戏元素")
        super().start_game()
    

if __name__ == '__main__':
    SnakeGame.start()