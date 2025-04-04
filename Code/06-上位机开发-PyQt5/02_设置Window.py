from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys

# 1. 创建应用程序
app = QApplication(sys.argv)

# 2. 创建窗口
w = QWidget()

# -------------------------------------------
# 设置窗口标题
w.setWindowTitle("黑马上位机")

# 设置窗口大小 800x600
# w.resize(640, 480)
w.setGeometry(100, 200, 800, 600)

# 设置图标
icon = QIcon("./qq.png")
w.setWindowIcon(icon)

# 添加气泡提示
w.setToolTip("我是窗口")
# -------------------------------------------

# 3. 显示窗口
w.show()

# 4. 等待窗口停止 execute 循环
sys.exit(app.exec_())