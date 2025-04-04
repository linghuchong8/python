from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys

def init_widget(w : QWidget):
    # 设置窗口标题
    w.setWindowTitle("组件")
    # w.setMinimumSize(200, 60)
    w.resize(480, 320)
    
    # 垂直盒子布局
    layout = QVBoxLayout()
    
    # ------------------------ 单行输入
    edit = QLineEdit()
    # 设置输入提示词
    edit.setPlaceholderText("请输入用户名")
    # 设置初始化内容
    edit.setText("张撒")
    # 读取文本内容
    print(edit.text())
    # 设置最大内容字符长度
    edit.setMaxLength(16)
    # 将组件添加到布局中
    layout.addWidget(edit)
    
    edit_pwd = QLineEdit()
    edit_pwd.setPlaceholderText("请输入密码")
    edit_pwd.setEchoMode(QLineEdit.Password)
    # 将组件添加到布局中
    layout.addWidget(edit_pwd)
    # ------------------------ 多行输入
    text_edit = QTextEdit()
    # 设置提示内容
    text_edit.setPlaceholderText("请输入个人简介")
    # 设置默认文本
    text_edit.setPlainText("我爱我的祖国")
    print(text_edit.toPlainText()) # 读取文本
    layout.addWidget(text_edit)

    # 设置布局
    w.setLayout(layout)

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
