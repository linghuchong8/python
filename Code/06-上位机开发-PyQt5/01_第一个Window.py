from PyQt5.QtWidgets import QApplication, QWidget
import sys

# 1. 创建应用程序
app = QApplication(sys.argv)

# 2. 创建窗口
w = QWidget()

# 3. 显示窗口
w.show()

# 4. 等待窗口停止 execute 循环
sys.exit(app.exec_())