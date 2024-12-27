from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap, QImage, QPalette, QColor
from io import BytesIO
from PIL import Image


class UiSendForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(428, 297)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 171, 61))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 281, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.background_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(-60, -40, 521, 341))
        self.background_label.setText("")
        self.background_label.setObjectName("background_label")
        self.result = QtWidgets.QLabel(parent=self.centralwidget)
        self.result.setGeometry(QtCore.QRect(20, 190, 231, 61))
        self.result.setStyleSheet("")
        self.result.setText("")
        self.result.setObjectName("result")
        self.send_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.send_btn.setGeometry(QtCore.QRect(270, 200, 121, 41))
        self.send_btn.setObjectName("send_btn")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 211, 41))
        self.label_2.setObjectName("label_2")
        self.amount = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.amount.setGeometry(QtCore.QRect(100, 131, 271, 31))
        self.amount.setObjectName("amount")
        self.background_label.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.result.raise_()
        self.send_btn.raise_()
        self.label_2.raise_()
        self.amount.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.load_fronted()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:24pt;\">Put address</span></p></body></html>"))
        self.send_btn.setText(_translate("MainWindow", "Send"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:24pt;\">Select amount</span></p></body></html>"))

    def load_fronted(self):
        self.background_label = self.findChild(QLabel, 'background_label')
        with open('images/background2.jpg', 'rb') as f:
            data = f.read()
        image = Image.open(BytesIO(data))
        image_data = image.tobytes("raw", "RGBA")
        q_image = QImage(image_data, image.size[0], image.size[1], QImage.Format.Format_RGBA8888)
        pixmap = QPixmap.fromImage(q_image)
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

        self.send_btn.setStyleSheet("""
                                    QPushButton {
                                        font-size: 24px;  /* Устанавливаем размер текста */
                                        color: #ffffff;  /* Устанавливаем цвет текста */
                                        background-color: #4CAF50;  /* Устанавливаем цвет фона */
                                        border: 2px solid #4CAF50;  /* Устанавливаем границу */
                                        border-radius: 10px;  /* Устанавливаем скругление углов */
                                    }
                                    QPushButton:hover {
                                        background-color: #45a049;  /* Изменяем цвет фона при наведении */
                                    }
                                """)

        palette = QPalette()

        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))

        self.label.setPalette(palette)
        self.label_2.setPalette(palette)
        self.result.setPalette(palette)
