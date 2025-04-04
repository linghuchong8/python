"""
PyQt5版GUI工具
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui.Ui_main_window import Ui_MainWindow
from views.upper_car_widget import UpperCarWidget
from views.serial_widget import SerialWidget
from views.bluetooth_widget import BluetoothWidget
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 创建对象
        self.ui = Ui_MainWindow()
        # 初始化内容
        self.ui.setupUi(self)
        # 初始化ui
        self.init_ui()

    def init_ui(self):
        # 动态的添加tab标签页
        self.ui.tabWidget.addTab(BluetoothWidget(self), "蓝牙助手")
        self.ui.tabWidget.addTab(SerialWidget(self), "串口助手")
        self.ui.tabWidget.addTab(UpperCarWidget(self), "串口上位机")
        # 选中蓝牙标签页
        # self.ui.tabWidget.setCurrentIndex(0)
        print(self.ui.tabWidget.count())
        self.ui.tabWidget.setCurrentIndex(self.ui.tabWidget.count() - 2)
        
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()