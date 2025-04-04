from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from PyQt5.QtWidgets import QWidget
# 帮我们直接运行此文件时，可以加载到上级目录的ui包
# sys.path.append("../")
from ui.Ui_my_regist_widget import Ui_RegisterWidget

# 自己的组件类Widget
class RegisterWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        # 加载生成好的ui内容
        self.ui = Ui_RegisterWidget()
        self.ui.setupUi(self)
        
        self.init_ui()

    def on_clicked(self):
        print('按钮按下！')

    def init_ui(self):
        self.ui.pushButton.clicked.connect(self.on_clicked)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 创建组件对象
    w = RegisterWidget()
    # 显示组件
    w.show()
    
    sys.exit(app.exec_())
