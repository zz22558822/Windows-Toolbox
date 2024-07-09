from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QApplication, QPushButton, QWidget
import subprocess
import winreg
import sys
import win32security
import win32api
import ctypes
import os



# 檢查是否為管理員權限
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False
if not is_admin():
    # 重新啟動程式以管理員權限
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit(1)

# 檢查檔案總管的註冊碼是否存在
def check_and_set_checkboxes(checkboxes):
    keys = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}"
    ]
    def check_registry_key(path):
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path):
                return True
        except FileNotFoundError:
            return False
    for key, checkbox in zip(keys, checkboxes):
            checkbox.setChecked(check_registry_key(key))


# 轉為exe 使用絕對路徑 解析img位置
def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)






class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 330)
        Form.setMinimumSize(QtCore.QSize(610, 330))
        Form.setMaximumSize(QtCore.QSize(610, 330))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(get_resource_path('img/LOGO.ico')), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 160, 210))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 32, 32))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(get_resource_path('img/night-mode.png')))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.checkBox3 = QtWidgets.QCheckBox(parent=self.widget)
        self.checkBox3.setGeometry(QtCore.QRect(20, 110, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        self.checkBox3.setFont(font)
        self.checkBox3.setChecked(True)
        self.checkBox3.setObjectName("checkBox3")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(60, 10, 80, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.checkBox4 = QtWidgets.QCheckBox(parent=self.widget)
        self.checkBox4.setGeometry(QtCore.QRect(20, 140, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        self.checkBox4.setFont(font)
        self.checkBox4.setChecked(True)
        self.checkBox4.setObjectName("checkBox4")
        self.checkBox1 = QtWidgets.QCheckBox(parent=self.widget)
        self.checkBox1.setGeometry(QtCore.QRect(20, 50, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        self.checkBox1.setFont(font)
        self.checkBox1.setCheckable(True)
        self.checkBox1.setChecked(True)
        self.checkBox1.setAutoRepeat(False)
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox2 = QtWidgets.QCheckBox(parent=self.widget)
        self.checkBox2.setGeometry(QtCore.QRect(20, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        self.checkBox2.setFont(font)
        self.checkBox2.setChecked(True)
        self.checkBox2.setObjectName("checkBox2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.widget_2 = QtWidgets.QWidget(parent=Form)
        self.widget_2.setGeometry(QtCore.QRect(180, 10, 200, 180))
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(60, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 32, 32))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(get_resource_path('img/key.png')))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton2 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton2.setGeometry(QtCore.QRect(10, 60, 85, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton3.setGeometry(QtCore.QRect(105, 60, 85, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton5 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton5.setGeometry(QtCore.QRect(105, 100, 85, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton5.setFont(font)
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton4 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton4.setGeometry(QtCore.QRect(10, 100, 85, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton4.setFont(font)
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton6 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton6.setGeometry(QtCore.QRect(10, 140, 181, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton6.setFont(font)
        self.pushButton6.setObjectName("pushButton6")
        self.widget_3 = QtWidgets.QWidget(parent=Form)
        self.widget_3.setGeometry(QtCore.QRect(390, 10, 210, 321))
        self.widget_3.setObjectName("widget_3")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 32, 32))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(get_resource_path('img/explorer.png')))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(60, 10, 111, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.checkBox8 = QtWidgets.QCheckBox(parent=self.widget_3)
        self.checkBox8.setGeometry(QtCore.QRect(10, 140, 90, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        self.checkBox8.setFont(font)
        self.checkBox8.setChecked(False)
        self.checkBox8.setObjectName("checkBox8")
        self.checkBox5 = QtWidgets.QCheckBox(parent=self.widget_3)
        self.checkBox5.setGeometry(QtCore.QRect(10, 50, 90, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        self.checkBox5.setFont(font)
        self.checkBox5.setCheckable(True)
        self.checkBox5.setChecked(False)
        self.checkBox5.setAutoRepeat(False)
        self.checkBox5.setObjectName("checkBox5")
        self.checkBox7 = QtWidgets.QCheckBox(parent=self.widget_3)
        self.checkBox7.setGeometry(QtCore.QRect(10, 110, 90, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        self.checkBox7.setFont(font)
        self.checkBox7.setChecked(False)
        self.checkBox7.setObjectName("checkBox7")
        self.checkBox10 = QtWidgets.QCheckBox(parent=self.widget_3)
        self.checkBox10.setGeometry(QtCore.QRect(120, 80, 90, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        self.checkBox10.setFont(font)
        self.checkBox10.setChecked(False)
        self.checkBox10.setObjectName("checkBox10")
        self.checkBox6 = QtWidgets.QCheckBox(parent=self.widget_3)
        self.checkBox6.setGeometry(QtCore.QRect(10, 80, 90, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        self.checkBox6.setFont(font)
        self.checkBox6.setChecked(False)
        self.checkBox6.setObjectName("checkBox6")
        self.checkBox11 = QtWidgets.QCheckBox(parent=self.widget_3)
        self.checkBox11.setGeometry(QtCore.QRect(120, 110, 90, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        self.checkBox11.setFont(font)
        self.checkBox11.setChecked(False)
        self.checkBox11.setObjectName("checkBox11")
        self.checkBox9 = QtWidgets.QCheckBox(parent=self.widget_3)
        self.checkBox9.setGeometry(QtCore.QRect(120, 50, 90, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        self.checkBox9.setFont(font)
        self.checkBox9.setCheckable(True)
        self.checkBox9.setChecked(False)
        self.checkBox9.setAutoRepeat(False)
        self.checkBox9.setObjectName("checkBox9")
        self.line = QtWidgets.QFrame(parent=self.widget_3)
        self.line.setGeometry(QtCore.QRect(0, 171, 210, 9))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.pushButton16 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton16.setGeometry(QtCore.QRect(40, 280, 61, 32))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton16.setFont(font)
        self.pushButton16.setObjectName("pushButton16")
        self.pushButton17 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton17.setGeometry(QtCore.QRect(140, 280, 61, 32))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton17.setFont(font)
        self.pushButton17.setObjectName("pushButton17")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(10, 280, 32, 32))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(get_resource_path('img/onedrive.png')))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(110, 280, 32, 32))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(get_resource_path('img/dropbox.png')))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton7 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton7.setGeometry(QtCore.QRect(120, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton7.setFont(font)
        self.pushButton7.setObjectName("pushButton7")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.widget_3)
        self.tabWidget.setGeometry(QtCore.QRect(0, 180, 211, 91))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton8 = QtWidgets.QPushButton(parent=self.tab_6)
        self.pushButton8.setGeometry(QtCore.QRect(5, 10, 95, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton8.setFont(font)
        self.pushButton8.setObjectName("pushButton8")
        self.pushButton9 = QtWidgets.QPushButton(parent=self.tab_6)
        self.pushButton9.setGeometry(QtCore.QRect(105, 10, 95, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton9.setFont(font)
        self.pushButton9.setObjectName("pushButton9")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton10 = QtWidgets.QPushButton(parent=self.tab_5)
        self.pushButton10.setGeometry(QtCore.QRect(5, 10, 95, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton10.setFont(font)
        self.pushButton10.setObjectName("pushButton10")
        self.pushButton11 = QtWidgets.QPushButton(parent=self.tab_5)
        self.pushButton11.setGeometry(QtCore.QRect(105, 10, 95, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton11.setFont(font)
        self.pushButton11.setObjectName("pushButton11")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton12 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton12.setGeometry(QtCore.QRect(5, 10, 95, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton12.setFont(font)
        self.pushButton12.setObjectName("pushButton12")
        self.pushButton13 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton13.setGeometry(QtCore.QRect(105, 10, 95, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton13.setFont(font)
        self.pushButton13.setObjectName("pushButton13")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton15 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton15.setGeometry(QtCore.QRect(105, 10, 95, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton15.setFont(font)
        self.pushButton15.setObjectName("pushButton15")
        self.pushButton14 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton14.setGeometry(QtCore.QRect(5, 10, 95, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton14.setFont(font)
        self.pushButton14.setObjectName("pushButton14")
        self.tabWidget.addTab(self.tab_2, "")
        self.widget_4 = QtWidgets.QWidget(parent=Form)
        self.widget_4.setGeometry(QtCore.QRect(180, 200, 201, 121))
        self.widget_4.setObjectName("widget_4")
        self.pushButton18 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton18.setGeometry(QtCore.QRect(10, 10, 181, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton18.setFont(font)
        self.pushButton18.setObjectName("pushButton18")
        self.pushButton19 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton19.setGeometry(QtCore.QRect(10, 45, 181, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton19.setFont(font)
        self.pushButton19.setObjectName("pushButton19")
        self.pushButton20 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton20.setGeometry(QtCore.QRect(10, 80, 181, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton20.setFont(font)
        self.pushButton20.setObjectName("pushButton20")
        self.widget_5 = QtWidgets.QWidget(parent=Form)
        self.widget_5.setGeometry(QtCore.QRect(10, 230, 161, 91))
        self.widget_5.setObjectName("widget_5")
        self.pushButton21 = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton21.setGeometry(QtCore.QRect(10, 10, 141, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton21.setFont(font)
        self.pushButton21.setObjectName("pushButton21")
        self.pushButton22 = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton22.setGeometry(QtCore.QRect(10, 50, 141, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton22.setFont(font)
        self.pushButton22.setObjectName("pushButton22")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)












        # 連接按鈕到執行函數
        self.pushButton.clicked.connect(self.execute_commands) #電源設定
        self.pushButton2.clicked.connect(self.get_windows_key_info) #Key 資訊
        self.pushButton3.clicked.connect(self.get_windows_activation_info) #Key 授權
        self.pushButton4.clicked.connect(self.get_windows_product_key) #當前序號
        self.pushButton5.clicked.connect(self.query_registry_product_key) #出廠序號
        self.pushButton6.clicked.connect(self.get_user_sid) #SID序號
        self.pushButton7.clicked.connect(self.select_all_button) #全選
        self.pushButton8.clicked.connect(self.hide_top_button) #資料夾上 隱藏
        self.pushButton9.clicked.connect(self.show_top_button) #資料夾上 顯示
        self.pushButton10.clicked.connect(self.hide_left_button) #本機左 隱藏
        self.pushButton11.clicked.connect(self.show_left_button) #本機左 顯示
        self.pushButton12.clicked.connect(self.hide_Quick_access) #快速存取 隱藏
        self.pushButton13.clicked.connect(self.show_Quick_access) #快速存取 顯示
        self.pushButton14.clicked.connect(self.hide_Internet) #網路 隱藏
        self.pushButton15.clicked.connect(self.show_Internet) #網路 顯示
        self.pushButton16.clicked.connect(self.hide_OneDrive) #隱藏 OneDrive
        self.pushButton17.clicked.connect(self.hide_Dropbox) # 隱藏 Dropbox
        self.pushButton18.clicked.connect(self.add_group_policy_packages) # 家用版安裝 gpedit
        self.pushButton19.clicked.connect(self.open_gpedit) # 開啟 gpedit
        self.pushButton20.clicked.connect(self.open_nteplwiz_password) # 開啟 Netplwiz 限制
        self.pushButton21.clicked.connect(self.modify_photo_viewer_file_associations) # 解鎖相片顯示器
        self.pushButton22.clicked.connect(self.run_sfc_scan) # 系統修復 SFC

        # 檢查檔案總管的註冊碼是否存在
        check_and_set_checkboxes([
            self.checkBox5, self.checkBox6, self.checkBox7,
            self.checkBox8, self.checkBox9, self.checkBox10, self.checkBox11
        ])










    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Windows Toolbox"))
        self.checkBox3.setText(_translate("Form", "  硬碟永不休眠"))
        self.label.setText(_translate("Form", "電源休眠"))
        self.checkBox4.setText(_translate("Form", "  螢幕永不關閉"))
        self.checkBox1.setText(_translate("Form", "  電腦永不睡眠"))
        self.checkBox2.setText(_translate("Form", "  電腦永不休眠"))
        self.pushButton.setText(_translate("Form", "執  行"))
        self.label_3.setText(_translate("Form", "Windows Key"))
        self.pushButton2.setText(_translate("Form", "Key 資訊"))
        self.pushButton3.setText(_translate("Form", "Key 授權"))
        self.pushButton5.setText(_translate("Form", "出廠序號"))
        self.pushButton4.setText(_translate("Form", "當前序號"))
        self.pushButton6.setText(_translate("Form", "SID 序號"))
        self.label_6.setText(_translate("Form", "檔案總管"))
        self.checkBox8.setText(_translate("Form", " 影片"))
        self.checkBox5.setText(_translate("Form", " 3D 物件"))
        self.checkBox7.setText(_translate("Form", " 文件"))
        self.checkBox10.setText(_translate("Form", " 下載"))
        self.checkBox6.setText(_translate("Form", " 音樂"))
        self.checkBox11.setText(_translate("Form", " 圖片"))
        self.checkBox9.setText(_translate("Form", " 桌面"))
        self.pushButton16.setText(_translate("Form", "隱藏"))
        self.pushButton17.setText(_translate("Form", "隱藏"))
        self.pushButton7.setText(_translate("Form", "全選"))
        self.pushButton8.setText(_translate("Form", "隱藏所選"))
        self.pushButton9.setText(_translate("Form", "顯示所選"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "資料夾(上)"))
        self.pushButton10.setText(_translate("Form", "隱藏所選"))
        self.pushButton11.setText(_translate("Form", "顯示所選"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "本機(左)"))
        self.pushButton12.setText(_translate("Form", "隱藏"))
        self.pushButton13.setText(_translate("Form", "顯示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "快速存取"))
        self.pushButton15.setText(_translate("Form", "顯示"))
        self.pushButton14.setText(_translate("Form", "隱藏"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "網路"))
        self.pushButton18.setText(_translate("Form", "家用版安裝 gpedit"))
        self.pushButton19.setText(_translate("Form", "開啟 gpedit"))
        self.pushButton20.setText(_translate("Form", "開啟 Netplwiz 限制"))
        self.pushButton21.setText(_translate("Form", "解鎖相片顯示器"))
        self.pushButton22.setText(_translate("Form", "系統修復 SFC"))




















    # 顯示資訊視窗
    def show_notification(self, title, message, size=None):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        # msg.setStandardButtons(QMessageBox.StandardButton.Ok) # 這邊是預設的 OK按鈕

        # 創建自定義的確定按鈕
        ok_button = msg.addButton("確認", QMessageBox.ButtonRole.AcceptRole)
        # 連接按鈕
        ok_button.clicked.connect(msg.accept)

        # 如果尺寸需要限制
        if size != None:
            msg.setStyleSheet(f"QLabel{{min-width:{size}px}}")

        msg.exec()
    # 顯示資訊視窗 複製版
    def show_notification_copy(self, title, message, size=None):
        msg = QMessageBox()
        # 設置不同的圖標類型
        msg.setIcon(QMessageBox.Icon.Information)  # 信息圖標
        # msg.setIcon(QMessageBox.Icon.Warning)     # 警告圖標
        # msg.setIcon(QMessageBox.Icon.Question)    # 問題圖標
        # msg.setIcon(QMessageBox.Icon.Critical)    # 錯誤圖標
        msg.setWindowTitle(title)
        msg.setText(message)

        # 創建自定義的確定按鈕
        ok_button = msg.addButton("確認", QMessageBox.ButtonRole.AcceptRole)
        copy_button = msg.addButton("複製", QMessageBox.ButtonRole.ActionRole)

        # 連接按鈕
        copy_button.clicked.connect(lambda: self.copy_to_clipboard(message))
        ok_button.clicked.connect(msg.accept)

        # 如果尺寸需要限制
        if size is not None:
            msg.setStyleSheet(f"QLabel{{min-width:{size}px}}")

        msg.exec()

    # 電源睡眠
    def execute_commands(self):
        commands_executed = []
        if self.checkBox1.isChecked():
            subprocess.run(["powercfg", "-change", "-standby-timeout-ac", "0"])
            commands_executed.append("電腦睡眠")
        if self.checkBox2.isChecked():
            subprocess.run(["powercfg", "-change", "-hibernate-timeout-ac", "0"])
            commands_executed.append("電腦休眠")
        if self.checkBox3.isChecked():
            subprocess.run(["powercfg", "-change", "-monitor-timeout-ac", "0"])
            commands_executed.append("螢幕關閉")
        if self.checkBox4.isChecked():
            subprocess.run(["powercfg", "-change", "-disk-timeout-ac", "0"])
            commands_executed.append("硬碟休眠")
        
        if commands_executed:
            message = "\n".join(commands_executed)
            self.show_notification("完成", message, 60)
        else:
            QMessageBox.critical(None, "錯誤", "請確認是否有選擇項目。")

    # Windows Key
    def get_windows_key_info(self): # 獲取 Key 資訊
        try:
            # 獲取詳細的資訊
            subprocess.Popen(["slmgr.vbs", "-dlv"], shell=True)

        except Exception as e:
            QMessageBox.critical(None, "錯誤", "查詢失敗，請嘗試其他方式。")

    def get_windows_activation_info(self): # 獲取 Key 授權
        try:
            # 獲取授權的資訊
            subprocess.Popen(["slmgr.vbs", "-xpr"], shell=True)

        except Exception as e:
            QMessageBox.critical(None, "錯誤", "查詢失敗，請嘗試其他方式。")

    def get_windows_product_key(self): #PowerShell wimc版本
        try:
            # 執行 wmic 命令並捕獲輸出
            result = subprocess.run(['wmic', 'path', 'softwarelicensingservice', 'get', 'OA3xOriginalProductKey', '/value'], capture_output=True, text=True)
            
            # 將輸出按行分割
            lines = result.stdout.splitlines()

            # 初始化序號
            product_key = None
            
            # 尋找包含序號的行
            for line in lines:
                if line.startswith("OA3xOriginalProductKey="):
                    # 提取序號部分
                    product_key = line.split('=')[1].strip()
                    break  # 找到序號，跳出迴圈

            # 檢查Windows序號
            if product_key:
                self.show_notification_copy("Windows 當前序號", product_key)
            else:
                QMessageBox.critical(None, "錯誤", "查詢失敗，請嘗試其他方式。")
                
        except Exception as e:
            # 捕獲其他潛在錯誤
            QMessageBox.critical(None, "錯誤", "查詢失敗，請嘗試其他方式。")

    def query_registry_product_key(self): # Regedit 版本
        try:
            # 打開註冊表鍵
            reg_key_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform"
            reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_key_path)
            
            # 獲取指定值
            value_name = "BackupProductKeyDefault"
            product_key, reg_type = winreg.QueryValueEx(reg_key, value_name)

            # 檢查Windows序號
            if product_key:
                self.show_notification_copy("Windows 當前序號", product_key)
            else:
                QMessageBox.critical(None, "錯誤", "查詢失敗，請嘗試其他方式。")

        except Exception as e:
            QMessageBox.critical(None, "錯誤", "查詢失敗，請嘗試其他方式。")

    def get_user_sid(self):# 獲取 SID
        try:
            user_name = win32api.GetUserName()
            domain_name = win32api.GetDomainName()
            sid_info = win32security.LookupAccountName(domain_name, user_name)
            user_sid = win32security.ConvertSidToStringSid(sid_info[0])
            
            # 檢查 SID
            if user_sid:
                self.show_notification_copy("Windows SID", user_sid)
            else:
                QMessageBox.critical(None, "錯誤", "查詢失敗，請嘗試其他方式。")

        except Exception as e:
            QMessageBox.critical(None, "錯誤", "查詢失敗，請嘗試其他方式。")

    # 檔案總管
    def select_all_button(self): # 選擇全部勾選
        for checkbox in [self.checkBox5, self.checkBox6, self.checkBox7,
                         self.checkBox8, self.checkBox9, self.checkBox10, self.checkBox11]:
            checkbox.setChecked(True)

    def hide_top_button(self): # 隱藏上方資料夾按鈕
        try:
            def del_Reg(guid):
                subprocess.run(f'reg delete "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{{{guid}}}" /f', shell=True, capture_output=True, text=True)
            if self.checkBox5.isChecked():
                del_Reg('0DB7E03F-FC29-4DC6-9020-FF41B59E513A')
            if self.checkBox6.isChecked():
                del_Reg('3dfdf296-dbec-4fb4-81d1-6a3438bcf4de')
            if self.checkBox7.isChecked():
                del_Reg('d3162b92-9365-467a-956b-92703aca08af')
            if self.checkBox8.isChecked():
                del_Reg('f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a')
            if self.checkBox9.isChecked():
                del_Reg('B4BFCC3A-DB2C-424C-B029-7FE99A87C641')
            if self.checkBox10.isChecked():
                del_Reg('088e3905-0323-4b02-9826-5d99428e115f')
            if self.checkBox11.isChecked():
                del_Reg('24ad3ad4-a569-4530-98e1-ab02f9417aa8')
            self.show_notification("成功", "隱藏上方資料夾，已完成，請重啟電腦後生效。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "隱藏時出現錯誤，請重新再試或改用指令。")

    def show_top_button(self): # 顯示上方資料夾按鈕
        try:
            def add_Reg(guid):
                subprocess.run(f'reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{{{guid}}}" /f', shell=True, capture_output=True, text=True)
            if self.checkBox5.isChecked():
                add_Reg('0DB7E03F-FC29-4DC6-9020-FF41B59E513A')
            if self.checkBox6.isChecked():
                add_Reg('3dfdf296-dbec-4fb4-81d1-6a3438bcf4de')
            if self.checkBox7.isChecked():
                add_Reg('d3162b92-9365-467a-956b-92703aca08af')
            if self.checkBox8.isChecked():
                add_Reg('f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a')
            if self.checkBox9.isChecked():
                add_Reg('B4BFCC3A-DB2C-424C-B029-7FE99A87C641')
            if self.checkBox10.isChecked():
                add_Reg('088e3905-0323-4b02-9826-5d99428e115f')
            if self.checkBox11.isChecked():
                add_Reg('24ad3ad4-a569-4530-98e1-ab02f9417aa8')
            self.show_notification("成功", "顯示上方資料夾，已完成，請重啟電腦後生效。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "取消隱藏時出現錯誤，請重新再試或改用指令。")

    def hide_left_button(self): # 隱藏左側本機按鈕
        try:
            def add_Reg(guid):
                subprocess.run(f'reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FolderDescriptions\\{{{guid}}}\\PropertyBag" /v ThisPCPolicy /t REG_SZ /d Hide /f', shell=True, capture_output=True, text=True)
            if self.checkBox5.isChecked():
                add_Reg('31C0DD25-9439-4F12-BF41-7FF4EDA38722')
            if self.checkBox6.isChecked():
                add_Reg('a0c69a99-21c8-4671-8703-7934162fcf1d')
            if self.checkBox7.isChecked():
                add_Reg('f42ee2d3-909f-4907-8871-4c22fc0bf756')
            if self.checkBox8.isChecked():
                add_Reg('35286a68-3c57-41a1-bbb1-0eae73d76c95')
            if self.checkBox9.isChecked():
                add_Reg('B4BFCC3A-DB2C-424C-B029-7FE99A87C641')
            if self.checkBox10.isChecked():
                add_Reg('7d83ee9b-2244-4e70-b1f5-5393042af1e4')
            if self.checkBox11.isChecked():
                add_Reg('0ddd015d-b06c-45d5-8c4c-f59713854639')
            self.show_notification("成功", "隱藏左側本機，已完成，請重啟電腦後生效。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "取消隱藏時出現錯誤，請重新再試或改用指令。")

    def show_left_button(self): # 顯示左側本機按鈕
        try:
            def add_Reg(guid):
                subprocess.run(f'reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FolderDescriptions\\{{{guid}}}\\PropertyBag" /v ThisPCPolicy /t REG_SZ /d Show /f', shell=True, capture_output=True, text=True)
            if self.checkBox5.isChecked():
                add_Reg('31C0DD25-9439-4F12-BF41-7FF4EDA38722')
            if self.checkBox6.isChecked():
                add_Reg('a0c69a99-21c8-4671-8703-7934162fcf1d')
            if self.checkBox7.isChecked():
                add_Reg('f42ee2d3-909f-4907-8871-4c22fc0bf756')
            if self.checkBox8.isChecked():
                add_Reg('35286a68-3c57-41a1-bbb1-0eae73d76c95')
            if self.checkBox9.isChecked():
                add_Reg('B4BFCC3A-DB2C-424C-B029-7FE99A87C641')
            if self.checkBox10.isChecked():
                add_Reg('7d83ee9b-2244-4e70-b1f5-5393042af1e4')
            if self.checkBox11.isChecked():
                add_Reg('0ddd015d-b06c-45d5-8c4c-f59713854639')
            self.show_notification("成功", "顯示左側本機，已完成，請重啟電腦後生效。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "取消隱藏時出現錯誤，請重新再試或改用指令。")

    def hide_OneDrive(self): # 隱藏 OneDrive
        try:
            guid = '018D5C66-4533-4307-9B53-224DE2ED1FE6'
            subprocess.run(f'reg delete "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Desktop\\NameSpace\\{{{guid}}}" /f', shell=True, capture_output=True, text=True)
            self.show_notification("成功", "隱藏 OneDrive 完成，請重啟電腦後生效。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "隱藏時出現錯誤，請重新再試。")

    def hide_Dropbox(self): # 隱藏 Dropbox
        try:
            guid = 'E31EA727-12ED-4702-820C-4B6445F28E1A'
            subprocess.run(f'reg delete "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Desktop\\NameSpace\\{{{guid}}}" /f', shell=True, capture_output=True, text=True)
            self.show_notification("成功", "隱藏 Dropbox 完成，請重啟電腦後生效。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "隱藏時出現錯誤，請重新再試。")

    def hide_Quick_access(self): # 隱藏快速存取
        try:
            subprocess.run('reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer" /v HubMode /t REG_DWORD /d 1 /f', shell=True, capture_output=True, text=True)
            self.show_notification("成功", "隱藏 快速存取 完成，請重啟電腦後生效。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "隱藏時出現錯誤，請重新再試。")

    def show_Quick_access(self): # 顯示快速存取
        try:
            subprocess.run('reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer" /v HubMode /t REG_DWORD /d 0 /f', shell=True, capture_output=True, text=True)
            self.show_notification("成功", "顯示 快速存取 完成，請重啟電腦後生效。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "顯示時出現錯誤，請重新再試。")

    def hide_Internet(self): # 隱藏網路
        try:
            guid = 'F02C1A0D-BE21-4350-88B0-7367FC96EF3C'
            subprocess.run(f'reg add "HKEY_CLASSES_ROOT\\CLSID\\{{{guid}}}\\ShellFolder" /v Attributes /t REG_DWORD /d b0940064 /f', shell=True, capture_output=True, text=True)
            self.show_notification("成功", "隱藏網路 完成，請重啟電腦後生效。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "隱藏時出現錯誤，請重新再試。")

    def show_Internet(self): # 顯示網路
        try:
            guid = 'F02C1A0D-BE21-4350-88B0-7367FC96EF3C'
            subprocess.run(f'reg add "HKEY_CLASSES_ROOT\\CLSID\\{{{guid}}}\\ShellFolder" /v Attributes /t REG_DWORD /d b0040064 /f', shell=True, capture_output=True, text=True)
            self.show_notification("成功", "顯示網路 完成，請重啟電腦後生效。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "顯示時出現錯誤，請重新再試。")


    # 家用版安裝 gpedit.msc
    def add_group_policy_packages(self):
        try:
            self.show_notification("請稍後", "安裝時間約 1～3 分鐘，依電腦速度而定。\n按下確認後開始安裝")

            # 執行 dir 命令，將結果寫入 List.txt
            list_file = os.path.join(get_resource_path('List.txt'))

            with open(list_file, 'w') as f:
                # 列出符合條件的文件並寫入List.txt
                for pattern in [
                    r"C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~3*.mum",
                    r"C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~3*.mum"
                ]:
                    result = subprocess.run(['dir', '/b', pattern], shell=True, capture_output=True, text=True)
                    f.write(result.stdout)
            # 讀取 List.txt 後執行dism命令
            with open(list_file, "r") as f:
                for line in f:
                    mum_file = line.strip()
                    if mum_file:
                        dism_command = f'dism /online /norestart /add-package:"C:\\Windows\\servicing\\Packages\\{mum_file}"'
                        subprocess.run(dism_command, shell=True)
            
            self.show_notification("成功", "家用版安裝 gpedit.msc 完成。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "發生不明錯誤，請重新再試。")

    # 家用版安裝 gpedit.msc For Bat
    def add_group_policy_packages_Bat(self):
        try:
            bat_content = '''
    @echo off
    pushd "%~dp0"
    dir /b %SystemRoot%\\servicing\\Packages\\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~3*.mum >List.txt
    dir /b %SystemRoot%\\servicing\\Packages\\Microsoft-Windows-GroupPolicy-ClientTools-Package~3*.mum >>List.txt
    for /f %%i in ('findstr /i . List.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\\servicing\\Packages\\%%i"
    pause
    '''

            # 將 BAT 內容寫入到檔案中
            bat_file = os.path.join(get_resource_path('run.bat'))
            with open(bat_file, 'w') as f:
                f.write(bat_content)

            # 使用 subprocess.Popen 執行 BAT 檔案
            subprocess.Popen(bat_file, shell=True)
            
            self.show_notification("成功", "已運行安裝 gpedit.msc。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "發生不明錯誤，請重新再試。")

    # 開啟 gpedit
    def open_gpedit(self):
        try:
            os.startfile("C:\\Windows\\System32\\gpedit.msc")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "啟動失敗，請確認是否有安裝 gpedit.msc。")

    # 開啟 Netplwiz 選項
    def open_nteplwiz_password(self):
        try:
            subprocess.run(['reg', 'add', r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\PasswordLess\Device', '/v', 'DevicePasswordLessBuildVersion', '/t', 'REG_DWORD', '/d', '1', '/f'], check=True)
            self.show_notification("成功", "解鎖 Netplwiz 選項完成。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "發生不明錯誤，請重新再試。")

    # 解鎖相片顯示器
    def modify_photo_viewer_file_associations(self):
        try:
            # 註冊表位置
            key_path = r"SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations"
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE)

            # 設定關聯
            file_types = {
                ".tif": "PhotoViewer.FileAssoc.Tiff",
                ".tiff": "PhotoViewer.FileAssoc.Tiff",
                "@": "",
                ".jpg": "PhotoViewer.FileAssoc.Tiff",
                ".jpeg": "PhotoViewer.FileAssoc.Tiff",
                ".png": "PhotoViewer.FileAssoc.Tiff",
                ".gif": "PhotoViewer.FileAssoc.Tiff",
                ".bmp": "PhotoViewer.FileAssoc.Tiff",
                ".ico": "PhotoViewer.FileAssoc.Tiff"
            }

            for ext, value in file_types.items():
                winreg.SetValueEx(key, ext, 0, winreg.REG_SZ, value)

            # 關閉註冊表
            winreg.CloseKey(key)

            self.show_notification("成功", "解鎖相片顯示器，已完成。")
        except Exception as e:
            QMessageBox.critical(None, "錯誤", "解鎖時出現錯誤，請重新再試或改用指令。")

    # 運行系統修復
    def run_sfc_scan(self):
        try:
            subprocess.Popen(['sfc.exe', '/scannow'], creationflags=subprocess.CREATE_NEW_CONSOLE)
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(None, "錯誤", "運行時出現錯誤，請重新再試或改用指令。")



















if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
