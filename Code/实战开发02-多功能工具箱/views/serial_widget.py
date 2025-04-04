from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import threading
# 帮我们直接运行此文件时，可以加载到上级目录的ui包
sys.path.append("../")

from ui.Ui_widget_serial import Ui_SerialWidget
from views.setting_dialog import SettingDialog
from drivers.driver_serial import *
from common.utils import *
"""
一、扫描并连接设备
二、获取用户输入，并发送数据
三、循环等待接收数据
四、显示接收到的数据

"""

class SerialWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window : QMainWindow = parent
        self.ui = Ui_SerialWidget()
        self.ui.setupUi(self)

        # 串口设备: 是None说明没有连接设备, 否则是SerialDevice对象
        self.current_serial_device : SerialDevice = None
        
        self.init_ui()
        
        self.refresh_devices()
    
    def __show_status(self, msg, msecs=0):
        if self.main_window is None:
            return
        
        # 确保parent是QMainWindow
        if isinstance(self.main_window, QMainWindow):
            self.main_window.statusBar().showMessage(msg, msecs)

    def refresh_devices(self):
        serial_ports = scan_serial_ports()
        if len(serial_ports) == 0:
            print("No serial serial_ports found.")
            self.__show_status("未发现串口设备")
            return
            
        print("Available serial serial_ports:")
        self.__show_status(f"发现串口设备: {len(serial_ports)}个", 2000)
        # 清理原有内容
        self.ui.cb_devices.clear()
        # 添加新的内容
        for device, description in serial_ports:
            print(device, "->", description)
            self.ui.cb_devices.addItem(description, userData=device)

    def on_refresh_click(self):
        print("刷新设备🔃")
        self.refresh_devices()
        
    def write_serial_data(self, data):
        """发送串口数据：会检查是否已连接
        :param data: 字节数组：可以是bytes、bytearray
        """
        # 判断是否是None
        if self.current_serial_device is None:
            print("请先连接设备")
            # 警告对话框
            QMessageBox.warning(self, "警告", "请先连接设备!")
            return
        # 定义字节数组bytearray 0x01 0x02 0x03
        # dat = bytearray([0x01, 0x02, 0x03])
        
        self.current_serial_device.write(data)
       
    def on_connect_click(self):
        if self.current_serial_device is not None:
            print("断开设备🔌")
            self.current_serial_device.close()
            self.current_serial_device = None
            self.ui.btn_connect.setText("连接🔗")
            self.ui.label_status.setPixmap(QPixmap(":/icon/disconnect"))
            return
        
        print("连接设备🔗")
        port = self.ui.cb_devices.currentData()
        
        # 如果没有选择设备, 直接返回
        if port is None:
            print("未选择设备")
            return
        
        # 获取被选择的设备
        print(f"index: {self.ui.cb_devices.currentIndex()}"
              f" text: {self.ui.cb_devices.currentText()}" 
              f" data: {port}")
        
        # 连接设备的波特率
        baudrate = int(self.ui.cb_baudrate.currentText())
        
        # 替换为您的串口名称、波特率和超时时间
        sp = SerialDevice(port, baud_rate=baudrate, timeout=None)  
        rst, msg = sp.open()
        if rst == False:
            print(msg)
            self.__show_status(f"设备连接失败: {port}")
            return

        print("成功:", msg)
        # 保存当前设备对象
        self.current_serial_device = sp
        # 显示设备状态
        self.__show_status(f"设备连接成功: {self.ui.cb_devices.currentText()}", 2000)
        self.ui.btn_connect.setText("断开🔌")
        self.ui.label_status.setPixmap(QPixmap(":/icon/connect"))
        
        # 开启循环接收任务
        thread = threading.Thread(target=self.start_receive_loop, daemon=True)
        thread.start()

    def start_receive_loop(self):
        try:
            # 开启循环接收任务
            while self.current_serial_device is not None:
                bytes_data = self.current_serial_device.readline()
                msg = decode_data(bytes_data)
                print("收到数据：", bytes_data, msg)
                # 显示接收到的数据
                # self.ui.text_receive.append(line.decode())
                self.ui.edit_recv.append(msg)
                # 自动滚动到最下边
                self.ui.edit_recv.moveCursor(QTextCursor.End)
        except:
            print("接收数据异常")
            self.current_serial_device = None
         
    def show_settings(self):
        print("show settings1")
        dialog = SettingDialog(self)
        # dialog.show() # 非阻塞方式弹出设置对话框
        rst = dialog.exec_() # 阻塞方式弹出设置对话框
        print("show settings: ", rst)
        if rst == QDialog.Accepted:
            print("保存数据:", dialog.baudrate)
            
    def on_send_click(self):
        # 获取用户输入的内容
        text = self.ui.edit_send.toPlainText()
        if len(text) == 0:
            print("请先输入要发送的数据")
            # 警告对话框
            QMessageBox.warning(self, "警告", "请先输入要发送的数据!")
            return
        
        # 发送数据
        self.write_serial_data(f"{text}\n".encode("utf-8"))
        
        # print(self.current_serial_device.read(300))

    def init_ui(self):
        self.ui.btn_setting.clicked.connect(self.show_settings)
        self.ui.btn_refresh.clicked.connect(self.on_refresh_click)
        self.ui.btn_connect.clicked.connect(self.on_connect_click)
        self.ui.btn_send.clicked.connect(self.on_send_click)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = SerialWidget()
    window.show()

    sys.exit(app.exec_())