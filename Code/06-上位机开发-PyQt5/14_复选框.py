from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QCheckBox, QLabel
from PyQt5.QtCore import Qt
import sys
import functools

def on_state_change(index, arg):
    print(index, end="-")
    if arg == Qt.Checked:
        print("选中")
    else:
        print("取消选择")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()
    
    # 配置窗口&给窗口添加内容
    w.setWindowTitle("复选框")
    w.resize(400, 100)
    layout = QHBoxLayout(w)
    
    btn1 = QCheckBox("抽烟")
    btn2 = QCheckBox("喝酒")
    btn3 = QCheckBox("烫头")
    btn2.setChecked(True)
    # 给btn1关联槽函数
    btn1.stateChanged.connect(lambda arg: on_state_change(1, arg))
    btn2.stateChanged.connect(lambda arg: on_state_change(2, arg))
    btn3.stateChanged.connect(functools.partial(on_state_change, 3))
    
    # 把组件添加到容器
    layout.addWidget(QLabel("谦哥的三大爱好:"))
    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)
    
    
    # 显示窗口
    w.show()

    sys.exit(app.exec_())