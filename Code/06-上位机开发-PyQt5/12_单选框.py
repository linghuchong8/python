from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout
import sys

def on_radio_button_toggled(arg, btn):
    print("on_toggled{}: {}".format(btn, arg))
    
# def on_toggled1(arg):
#     # print("on_toggled1: ", arg)
#     on_radio_button_toggled(arg, 1)
    
# def on_toggled2(arg):
#     # print("on_toggled2: ", arg)
#     on_radio_button_toggled(arg, 2)
    
# def on_toggled3(arg):
#     # print("on_toggled3: ", arg)
#     on_radio_button_toggled(arg, 3)
    
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
    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)
    
    # 给组件切换信号添加槽函数 (lambda就是没有名字的函数)
    # btn1.toggled.connect(on_toggled1)
    # btn2.toggled.connect(on_toggled2)
    # btn3.toggled.connect(on_toggled3)
    btn1.toggled.connect(lambda arg: on_radio_button_toggled(arg, 1))
    btn2.toggled.connect(lambda arg: on_radio_button_toggled(arg, 2))
    btn3.toggled.connect(lambda arg: on_radio_button_toggled(arg, 3))
    
    # 设置选中指定按钮
    btn1.setChecked(True)
    
    # 显示窗口
    w.show()

    sys.exit(app.exec_())