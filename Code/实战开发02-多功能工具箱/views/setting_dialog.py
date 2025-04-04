
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

sys.path.append("..")

from ui.Ui_dialog_setting import Ui_SettingDialog

class SettingDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingDialog()
        self.ui.setupUi(self)

        # 可以通过此设置，固定对话框的大小
        self.setFixedSize(self.width(), self.height())
        
        self.initUi()

        self.baudrate = None

    def initUi(self):
        pass

    def accept(self):
        super().accept()
        print("accept")
        # 读取当前波特率的设置值
        self.baudrate = self.ui.cb_baudrate.currentText()
        # 保存数据到文件

    def reject(self):
        super().reject()
        print("reject")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = SettingDialog()
    dialog.show()
    sys.exit(app.exec_())