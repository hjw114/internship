"""
这个写得不太好
用的时候要把图片和应用的地址都改成自己电脑端的
（不知道为什么相对路径老是失败，我用了绝对路径）
"""
import os
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
import sys
import webbrowser

class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.label_1 = QLabel(self)
        self.label_2 = QLabel(self)
        self.label_3 = QLabel(self)
        self.label_4 = QLabel(self)
        self.label_1.setPixmap(QPixmap("D:/Python Project/demo2/venv/qq_icon.PNG"))
        self.label_2.setPixmap(QPixmap("D:/Python Project/demo2/venv/wyy_icon.PNG"))
        self.label_3.setPixmap(QPixmap("D:/Python Project/demo2/venv/vx_icon.PNG"))
        self.label_4.setPixmap(QPixmap("D:/Python Project/demo2/venv/steam_icon.PNG"))
        self.label_1.mousePressEvent = self.photo_link_1
        self.label_2.mousePressEvent = self.photo_link_2  # 设置图片点击事件
        self.label_3.mousePressEvent = self.photo_link_3
        self.label_4.mousePressEvent = self.photo_link_4

        self.hbox1 = QHBoxLayout()  # 设置箱布局
        self.setLayout(self.hbox1)
        self.hbox1.addWidget(self.label_1)
        self.hbox1.addWidget(self.label_2)
        self.hbox1.addWidget(self.label_3)
        self.hbox1.addWidget(self.label_4)

    def initUI(self):
        self.resize(500, 300)  # 调整窗口的大小
        self.center()
        self.setWindowTitle('Quick Start')  # 设置窗口的标题
        self.show()  # 显示在屏幕上

    # 控制窗口显示在屏幕中心的方法
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def photo_link_1(self, test):
        Path = r'D:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe'
        os.startfile(Path)

    def photo_link_2(self, test):
        Path = r'C:\Program Files (x86)\Netease\CloudMusic\cloudmusic.exe'
        os.startfile(Path)

    def photo_link_3(self, test):
        Path = r'D:\Program Files (x86)\Tencent\WeChat\WeChat.exe'
        os.startfile(Path)

    def photo_link_4(self, test):
        Path = r'F:\Steam\Steam.exe'
        os.startfile(Path)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个应用程序对象
    win = WindowDemo()
    win.show()  # 窗口显示在屏幕上
    sys.exit(app.exec_())   # 确保应用程序干净的退出