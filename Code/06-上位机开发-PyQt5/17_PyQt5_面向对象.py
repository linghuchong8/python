from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from PyQt5.QtWidgets import QWidget

# 自己的组件类Widget
class MyWidget(QWidget):
    
    def __init__(self, title="窗口标题"):
        super().__init__()
        self.setWindowTitle(title)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
    	# ---------------------------------

        # 在这里初始化界面内容
        # layout.addWidget(QLabel("文本"))
        # layout.addWidget(QPushButton("按钮1"))
        
    	# ---------------------------------
        self.setLayout(layout)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 创建组件对象
    w = MyWidget("我的窗口")
    # 显示组件
    w.show()
    
    sys.exit(app.exec_())
