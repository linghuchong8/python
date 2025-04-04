from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import sys
import functools

def on_clicked():
    text, confirm = QInputDialog.getText(w, "提示", "请输入角色名称")
    if confirm:
        nike_name_label.setText(text)
    # 选择一个txt文件
    # rst = QtWidgets.QFileDialog.getOpenFileName(w, "选择文件", "", "Text Files (*.txt)")
    # print(rst)
    # 选择一个颜色
    # color = QtWidgets.QColorDialog.getColor()
    # print(color.name())
    # 选择字体
    # font, ok = QtWidgets.QFontDialog.getFont()
    # if ok:
    #     print(font.toString())
    #     print(font.family())
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()
    
    # 配置窗口&给窗口添加内容
    w.setWindowTitle("复选框")
    w.resize(400, 100)
    
    layout = QVBoxLayout(w)
    
    nike_name_label = QLabel("匿名")
    
    btn = QPushButton("创建角色")
    btn.clicked.connect(on_clicked)
    
    layout.addWidget(nike_name_label)
    layout.addWidget(btn)
    
    # 显示窗口
    w.show()

    sys.exit(app.exec_())