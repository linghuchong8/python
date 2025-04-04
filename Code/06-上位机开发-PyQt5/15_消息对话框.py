from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
import sys
import functools

def on_clicked():
    print("弹出对话框")
    # rst = QMessageBox.information(w, "消息对话框", "删除后无法恢复")
    # print("rst: ", rst)
    
    result = QMessageBox.question(
        w, "删除提示", "确认要删除好友吗?",
        buttons = QMessageBox.Ok | QMessageBox.Cancel,
        defaultButton= QMessageBox.Cancel
    )

    print("result: ", result)
    if result == QMessageBox.Ok:
        print('删除好友')
    else:
        print("取消删除")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()
    
    # 配置窗口&给窗口添加内容
    w.setWindowTitle("复选框")
    w.resize(400, 100)
    
    btn = QPushButton("删除好友")
    btn.clicked.connect(on_clicked)
    btn.setParent(w)
    
    # 显示窗口
    w.show()

    sys.exit(app.exec_())