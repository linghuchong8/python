from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QButtonGroup
import sys

def on_group_toggled(btn: QRadioButton):
    print(btn.text(), btn.isChecked())
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()
    
    # 配置窗口&给窗口添加内容
    w.setWindowTitle("单选框")
    w.resize(400, 100)
    layout = QHBoxLayout(w)
    
    btn1 = QRadioButton("男")
    btn2 = QRadioButton("女")
    btn3 = QRadioButton("妖")
    # 设置选中指定按钮
    btn1.setChecked(True)
    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)
    
    # 给一个组添加事件
    group = QButtonGroup(w)
    group.addButton(btn1)
    group.addButton(btn2)
    group.addButton(btn3)
    group.buttonToggled.connect(on_group_toggled)
    
    # 显示窗口
    w.show()

    sys.exit(app.exec_())