from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
import sys

def init_widget(w : QWidget):
    # 设置窗口标题
    w.setWindowTitle("组件")
    # w.resize(300, 400)

    label = QLabel(w)
    pixmap = QPixmap("./img.png")
    label.setPixmap(pixmap)
    # 根据图片大小,设置窗口大小
    w.resize(pixmap.width(), pixmap.height())

if __name__ == '__main__':
    # 1. 创建应用程序
    app = QApplication(sys.argv)

    # 2. 创建窗口
    w = QWidget()

    # -------------------------------------------
    init_widget(w)
    # -------------------------------------------

    # 3. 显示窗口
    w.show()

    # 4. 等待窗口停止 execute 循环
    sys.exit(app.exec_())
