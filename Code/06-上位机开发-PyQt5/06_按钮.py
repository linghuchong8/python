from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys

def click_event():
    print("发射火箭！🚀")

def init_widget(w: QWidget):
    
    w.setWindowTitle("按钮")
    
    btn = QPushButton("发射")
    btn.setParent(w)
    btn.setText("点击发射")
    # 给按钮的点击信号，添加(关联)槽函数
    btn.clicked.connect(click_event)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()
    
    # 配置窗口&给窗口添加内容
    init_widget(w)
    
    # 显示窗口
    w.show()

    sys.exit(app.exec_())