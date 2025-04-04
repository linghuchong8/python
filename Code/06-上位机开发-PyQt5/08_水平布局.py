from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
import sys


def init_widget(w: QWidget):
    
    w.setWindowTitle("水平布局")
    
    btn1 = QPushButton("发射1")
    btn2 = QPushButton("发射2")
    btn3 = QPushButton("发射3")
    btn4 = QPushButton("发射4")
    btn5 = QPushButton("发射5")
    # 创建布局 Horizontal 水平 Vertical 竖直
    layout = QHBoxLayout()
    # 给QWidget容器设置内容布局方式
    w.setLayout(layout)
    
    # 将按钮添加到布局中
    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)
    layout.addWidget(btn4)
    layout.addWidget(btn5)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()
    
    # 配置窗口&给窗口添加内容
    init_widget(w)
    
    # 显示窗口
    w.show()

    sys.exit(app.exec_())