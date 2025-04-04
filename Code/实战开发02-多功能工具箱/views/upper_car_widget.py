from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
# 帮我们直接运行此文件时，可以加载到上级目录的ui包
sys.path.append("../")

from ui.Ui_widget_upper_car import Ui_UpperCarWidget
from drivers.driver_serial import *

"""
1. 扫描串口设备
2. 连接串口设备(更新按钮状态)
3. 断开连接
4. 发送各种控制指令+数据

"""



class UpperCarWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window : QMainWindow = parent
        self.ui = Ui_UpperCarWidget()
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
        # 判断是否是None
        if self.current_serial_device is None:
            print("请先连接设备")
            # 警告对话框
            QMessageBox.warning(self, "警告", "请先连接设备!")
            return
        # 定义字节数组bytearray 0x01 0x02 0x03
        # dat = bytearray([0x01, 0x02, 0x03])
        
        self.current_serial_device.write(data)
        
        # 如果有阻塞的任务, 会将整个界面卡死
        # 解决办法: 在子线程做耗时任务(异步任务)
        # line = self.current_serial_device.read(2)
        # line = self.current_serial_device.readline()
        # print(line)  # 读取一行数据

    def on_connect_click(self):
        if self.current_serial_device is not None:
            print("断开设备🔌")
            self.current_serial_device.close()
            self.current_serial_device = None
            self.ui.btn_connect.setText("连接🔗")
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
        self.current_serial_device = sp
        self.ui.btn_connect.setText("断开🔌")

    def on_light_click(self):
        print('车灯开关')
        self.write_serial_data(b"\x01")

    def on_buzzer_click(self):
        print('车蜂鸣器')
        self.write_serial_data(b"\x02")
        
    def on_forward_speed_change(self, value):
        print(f"前进速度: {value}")
        # arr = [value]
        # 声明字节数组
        arr = bytearray([0x13, value])
        # 把bytearray转成bytes
        # arr = bytes(arr)
        # 发送数据
        self.write_serial_data(arr)
        # self.write_serial_data(b"\x13" + bytes([value]))

    def init_ui(self):
        self.ui.btn_refresh.clicked.connect(self.on_refresh_click)
        self.ui.btn_connect.clicked.connect(self.on_connect_click)
        self.ui.btn_light.clicked.connect(self.on_light_click)
        self.ui.btn_buzzer.clicked.connect(self.on_buzzer_click)
        self.ui.btn_forward.clicked.connect(lambda: self.write_serial_data(b"\x03"))
        self.ui.btn_backward.clicked.connect(lambda: self.write_serial_data(b"\x04"))
        self.ui.btn_move_left.clicked.connect(lambda: self.write_serial_data(b"\x05"))
        self.ui.btn_move_right.clicked.connect(lambda: self.write_serial_data(b"\x06"))
        self.ui.btn_stop.clicked.connect(lambda: self.write_serial_data(b"\x07"))
        self.ui.slider_forward_speed.valueChanged.connect(self.on_forward_speed_change)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = UpperCarWidget()
    window.show()

    sys.exit(app.exec_())