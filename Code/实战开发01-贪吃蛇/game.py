from abc import abstractmethod
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

COLOR_GRAY = QtGui.QColor(128, 128, 128)
COLOR_RED  = QtGui.QColor(255, 0, 0)
COLOR_GREEN = QtGui.QColor(0, 255, 0)
COLOR_BLUE = QtGui.QColor(0, 0, 255)
COLOR_WHITE = QtGui.QColor(255, 255, 255)
COLOR_BLACK = QtGui.QColor(0, 0, 0)

class Game(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game")
        
        self.timer = QtCore.QBasicTimer()
        self.fps = 2
        self.delay = 1000 // self.fps
        self.is_game_over = False
        
    def set_fps(self, fps):
        self.delay = 1000 // fps
        self.fps = fps
        if self.timer.isActive():
            self.timer.stop()
            self.timer.start(self.delay, self)
        
    def timerEvent(self, event):
        if self.is_game_over:
            self.timer.stop()
        else:
            self.on_time_event(event)
        
        self.repaint()
        
    @abstractmethod
    def on_time_event(self):
        pass
        
    @abstractmethod
    def draw_content(self, qp: QtGui.QPainter):
        pass
    
    def paintEvent(self, event: QtGui.QPaintEvent):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw_content(qp)
        qp.end()
        
    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
            return
        elif event.key() == QtCore.Qt.Key_Space:
            if self.is_game_over:
                self.start_game()
                return
            
        super().keyPressEvent(event)
        
    def start_game(self):
        self.is_game_over = False
        self.timer.start(self.delay, self)
        
    @classmethod
    def start(cls):
        app = QtWidgets.QApplication(sys.argv)
        # 创建cls的对象
        game = cls()
        game.start_game()
        game.show()
        # while (1)
        sys.exit(app.exec_())