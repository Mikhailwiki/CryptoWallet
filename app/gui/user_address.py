from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap, QImage, QPalette, QColor
from io import BytesIO
from PIL import Image


class UiUsersAddress(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(475, 324)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 211, 51))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 110, 341, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.background_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(-60, -40, 571, 361))
        self.background_label.setText("")
        self.background_label.setObjectName("background_label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 100, 41, 41))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.background_label.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 21))
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
                                      "<html><head/><body><p><span style=\" font-size:24pt;\">Your address</span></p></body></html>"))

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

        palette = QPalette()

        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))

        self.label.setPalette(palette)
