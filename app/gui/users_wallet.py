from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap, QImage
from io import BytesIO
from PIL import Image


class UiUsersWallet(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(-20, 0, 821, 591))
        self.background_label.setText("")
        self.background_label.setObjectName("background_label")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 190, 461, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.send_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.send_btn.setObjectName("send_btn")
        self.gridLayout.addWidget(self.send_btn, 1, 1, 1, 1)
        self.get_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.get_btn.setObjectName("get_btn")
        self.gridLayout.addWidget(self.get_btn, 1, 0, 1, 1)
        self.update_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.update_btn.setObjectName("update_btn")
        self.gridLayout.addWidget(self.update_btn, 2, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(parent=self.gridLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 3, 0, 1, 2)
        self.delete_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.delete_btn.setObjectName("delete_btn")
        self.gridLayout.addWidget(self.delete_btn, 0, 0, 1, 2)
        self.login = QtWidgets.QLabel(parent=self.centralwidget)
        self.login.setGeometry(QtCore.QRect(10, 10, 351, 51))
        self.login.setText("")
        self.login.setObjectName("login")
        self.excange_rate = QtWidgets.QLabel(parent=self.centralwidget)
        self.excange_rate.setGeometry(QtCore.QRect(460, -20, 321, 311))
        self.excange_rate.setText("")
        self.excange_rate.setObjectName("excange_rate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
                                      "<html><head/><body><p><span style=\" font-size:24pt;\">Wallet</span></p></body></html>"))
        self.send_btn.setText(_translate("MainWindow", "Send"))
        self.get_btn.setText(_translate("MainWindow", "Get"))
        self.update_btn.setText(_translate("MainWindow", "Update"))
        self.delete_btn.setText(_translate("MainWindow", "Delete Account"))

    def load_fronted(self):
        self.background_label = self.findChild(QLabel, 'background_label')
        try:
            with open('images/background2.jpg', 'rb') as f:
                data = f.read()
            image = Image.open(BytesIO(data))
            image_data = image.tobytes("raw", "RGBA")
            q_image = QImage(image_data, image.size[0], image.size[1], QImage.Format.Format_RGBA8888)
            pixmap = QPixmap.fromImage(q_image)
            self.background_label.setPixmap(pixmap)
            self.background_label.setScaledContents(True)

            with open('images/temp_background.jpg', 'wb') as f:
                f.write(data)

            self.listWidget.setStyleSheet(f"""
                        QListWidget {{
                            background-image: url(images/temp_background.jpg);
                            background-repeat: no-repeat;
                            background-position: center;
                            background-size: cover;  /* Растягиваем изображение на весь фон */
                            border: 1px solid #d0d0d0;
                        }}
                        QListWidget::item {{
                            background-color: rgba(255, 255, 255, 128);
                            border-bottom: 1px solid #d0d0d0;
                        }}
                        QListWidget::item:selected {{
                            background-color: rgba(160, 160, 160, 128);
                            color: #ffffff;
                        }}
                    """)

            self.update_btn.setStyleSheet("""
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

            self.get_btn.setStyleSheet("""
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

            self.delete_btn.setStyleSheet("""
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
        except Exception as e:
            print(f"Error loading frontend: {e}")
