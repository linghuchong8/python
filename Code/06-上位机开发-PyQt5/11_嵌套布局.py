from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout
import sys

    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()
    
    # 配置窗口&给窗口添加内容
    
    w.setWindowTitle("嵌套布局")
    root_layout = QHBoxLayout(w)
    
    layout1 = QVBoxLayout()
    layout1.addWidget(QPushButton("1"))
    
    layout2 = QVBoxLayout()
    layout2.addWidget(QPushButton("1"))
    layout2.addWidget(QPushButton("2"))
    
    layout3 = QVBoxLayout()
    layout3.addWidget(QPushButton("1"))
    layout3.addWidget(QPushButton("2"))
    layout3.addWidget(QPushButton("3"))
    
    layout4 = QVBoxLayout()
    layout4.addWidget(QPushButton("1"))
    layout4.addWidget(QPushButton("2"))
    layout4.addWidget(QPushButton("3"))
    layout4.addWidget(QPushButton("4"))
    
    root_layout.addLayout(layout1)
    root_layout.addLayout(layout2)
    root_layout.addLayout(layout3)
    root_layout.addLayout(layout4)
    
    # 显示窗口
    w.show()

    sys.exit(app.exec_())