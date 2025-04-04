from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFormLayout
import sys


def on_submit():
    print("提交")
    print("用户名", edit_username.text())
    print("密码", edit_password.text())
    print("手机号", edit_phone.text())
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()
    
    # 配置窗口&给窗口添加内容
    
    w.setWindowTitle("表单布局")
    w.resize(400, 300)
    
    # 创建布局
    layout = QFormLayout(w)
    # w.setLayout(layout)
    # 创建组件
    edit_username = QLineEdit()
    edit_password = QLineEdit()
    edit_password.setEchoMode(QLineEdit.Password)
    edit_phone    = QLineEdit()
    btn_sumbit    = QPushButton("提交")
    btn_sumbit.clicked.connect(on_submit)
    layout.addRow("用户名", edit_username)
    layout.addRow("密码", edit_password)
    layout.addRow("手机号", edit_phone)
    layout.addRow(btn_sumbit)
    
    # 显示窗口
    w.show()

    sys.exit(app.exec_())