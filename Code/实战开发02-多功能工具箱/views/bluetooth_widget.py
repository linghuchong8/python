from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
import sys
# 帮我们直接运行此文件时，可以加载到上级目录的ui包
sys.path.append("../")

from common.utils import decode_data
from drivers.driver_bluetooth import BluetoothDataTransfer
from ui.Ui_widget_bluetooth import Ui_BluetoothWidget

"""
PyQt中自定义信号和槽的步骤如下：

1.  定义信号：在类中定义一个信号，使用PyQt的信号机制可以实现自定义信号。可以通过pyqtSignal()方法来创建一个信号对象。pyqtSignal参数槽函数的参数类型
2.  定义槽：在类中定义一个槽函数，使用@pyqtSlot()装饰器将该方法注册为槽函数。 
3.  连接信号和槽：使用信号.connect(槽函数)方法将信号和槽连接起来。 
4.  触发信号：在需要触发信号的地方，使用信号.emit()方法来触发该信号，参数和槽函数参数一致。
"""


class BluetoothWidget(QWidget):
    
    # 1. 定义信号：
    scan_device_signal = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window : QMainWindow = parent
        self.ui = Ui_BluetoothWidget()
        self.ui.setupUi(self)
        
        self.current_bdt: BluetoothDataTransfer = None
        # 3.  连接信号和槽：
        self.scan_device_signal.connect(self.on_scan_device_result)

        self.init_ui()
        
        # 默认隐藏
        self.ui.gb_connected_device.setVisible(False)
        
    def __show_status(self, msg, msecs=0):
        if self.main_window is None:
            return
        
        # 确保parent是QMainWindow
        if isinstance(self.main_window, QMainWindow):
            self.main_window.statusBar().showMessage(msg, msecs)
            
    # def on_btn_connect_clicked(self, arg=""):
    #     print("连接🔗", arg)
    
    def refresh_devices(self):
        print("刷新🔃", threading.current_thread().name)
        devices = BluetoothDataTransfer.scan_devices()
        # 4.  触发信号：
        # self.on_scan_device_result(devices)
        self.scan_device_signal.emit(devices)
        
    # 2.  定义槽：
    @pyqtSlot(list)
    def on_scan_device_result(self, devices: list):
        print("更新UI线程:", threading.current_thread().name) 
        
        # pyqt5:建议在主线程更新UI
        
        self.__show_status(f"扫描到{len(devices)}个设备")
        
        # 启用刷新按钮
        self.ui.btn_refresh.setEnabled(True)
        
        # 把扫描到的设备加入到下拉列表中
        self.ui.cb_devices.clear()
        # 循环所有设备
        for device in devices:
            # addr, name = device
            self.ui.cb_devices.addItem(device[1], device)
            
        # 默认选中第一个设备
        if self.ui.cb_devices.count() > 0:
            self.ui.cb_devices.setCurrentIndex(0)
    
    def on_refresh_clicked(self):
        # 禁用掉刷新按钮，避免重复进入刷新
        self.ui.btn_refresh.setEnabled(False)
        
        # rst = threading.Thread(target=BluetoothDataTransfer.scan_devices).start()
        thread = threading.Thread(target=self.refresh_devices, daemon=True)
        thread.start()
        
    
    def on_connect_clicked(self):
        if self.current_bdt is not None:
            print("断开连接：", self.current_bdt.target_name)
            self.current_bdt.disconnect()
            self.__show_status(f"已断开{self.current_bdt.target_name}的连接", 2000)
            self.current_bdt = None
            self.ui.btn_connect.setText("连接🔗")
            self.ui.label_state.setPixmap(QPixmap(":/icon/disconnect"))
            self.ui.gb_connected_device.setVisible(False)
            return
            
        print("连接🔗")
        device = self.ui.cb_devices.currentData()
        if device is None:
            print("请先扫描并选择设备！")
            QMessageBox.warning(self, "警告", "请先扫描并选择设备！", QMessageBox.Yes)
            return
        
        addr, name = device
        bdt = BluetoothDataTransfer(addr, name)
        # bdt = BluetoothDataTransfer(*device)
        if bdt.connect():
            self.ui.btn_connect.setText("断开🔌")
            self.ui.label_state.setPixmap(QPixmap(":/icon/connect"))
            self.ui.label_addr.setText(f"名称:{name}")
            self.ui.label_name.setText(f"地址:{addr}")
            self.ui.gb_connected_device.setVisible(True) # 修改可见状态
            self.__show_status(f"已连接{name}的设备")
            
            self.current_bdt = bdt
            
            thread = threading.Thread(target=self.recv_msg_loop, daemon=True)
            thread.start()
            
    def recv_msg_loop(self):
        while True:
            # 如果设备已断开, 则退出循环
            if self.current_bdt is None:
                break
            
            data = self.current_bdt.receive_data()
            if data:
                print("data->", data)
                self.ui.edit_recv.append(decode_data(data))
            else:
                # 对方关闭连接, 退出循环
                break
            
    @pyqtSlot()
    def on_send_clicked(self):
        # 检查是否有连接的设备
        if self.current_bdt is None:
            print("请先连接设备！")
            QMessageBox.warning(self, "警告", "请先连接设备！", QMessageBox.Yes)
            return
        
        # 获取输入框的内容（判定是否输入了内容）
        text = self.ui.edit_send.toPlainText()
        if text == "":
            print("请输入要发送的内容！")
            QMessageBox.warning(self, "警告", "请输入要发送的内容！", QMessageBox.Yes)
            return
        
        # 支持直接发送字符串(默认UTF-8编码), 也可以发送字节流(字节数组)
        # self.current_bdt.send_data(text.encode())
        # self.current_bdt.send_data(b"\xAF\x13")
        self.current_bdt.send_data(text.encode("gbk"))

    def init_ui(self):
        self.ui.btn_connect.clicked.connect(self.on_connect_clicked)
        self.ui.btn_refresh.clicked.connect(self.on_refresh_clicked)
        self.ui.btn_send.clicked.connect(self.on_send_clicked)
        self.ui.btn_send_clear.clicked.connect(self.ui.edit_send.clear)
        self.ui.btn_recv_clear.clicked.connect(self.ui.edit_recv.clear)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = BluetoothWidget()
    window.show()

    sys.exit(app.exec_())