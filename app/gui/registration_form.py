from PyQt6 import QtCore, QtWidgets
from io import BytesIO
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QImage, QPixmap
from PIL import Image


class UiRegistrationForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 552)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(-70, -50, 901, 631))
        self.background_label.setText("")
        self.background_label.setObjectName("background_label")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 110, 381, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.log_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.log_btn.setObjectName("log_btn")
        self.horizontalLayout.addWidget(self.log_btn)
        self.sign_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.sign_btn.setObjectName("sign_btn")
        self.horizontalLayout.addWidget(self.sign_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 2, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.result = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.result.setText("")
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.load_background_image()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.log_btn.setText(_translate("MainWindow", "Log in"))
        self.sign_btn.setText(_translate("MainWindow", "Sign up"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label.setText(_translate("MainWindow", "Login"))

    def load_background_image(self):
        self.background_label = self.findChild(QLabel, 'background_label')
        try:
            with open('images/background.jpg', 'rb') as f:
                data = f.read()
            image = Image.open(BytesIO(data))
            image_data = image.tobytes("raw", "RGBA")
            q_image = QImage(image_data, image.size[0], image.size[1], QImage.Format.Format_RGBA8888)
            pixmap = QPixmap.fromImage(q_image)
            self.background_label.setPixmap(pixmap)
            self.background_label.setScaledContents(True)
        except Exception as e:
            print(f"Error loading background image: {e}")
