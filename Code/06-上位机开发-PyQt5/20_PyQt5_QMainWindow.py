from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from PyQt5.QtWidgets import QMainWindow
from ui.Ui_main_window import Ui_MainWindow

# 自己的组件类Widget
class MyMainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        # 加载生成好的ui内容
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.init_ui()
        
    def on_click(self):
        # 状态栏显示内容
        self.statusBar().showMessage("消息发送中...", 1000)
        
    def init_ui(self):
        self.ui.btn_status_bar.clicked.connect(self.on_click)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 创建组件对象
    w = MyMainWindow()
    # 显示组件
    w.show()
    
    sys.exit(app.exec_())
