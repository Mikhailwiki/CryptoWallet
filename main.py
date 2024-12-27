import sqlite3
import hashlib
import sys
import os

import pyperclip
import requests
import secrets
from prettytable import PrettyTable

from app.CONSTS import SPECIAL_CHARACTERS

from app.gui.registration_form import UiRegistrationForm
from app.gui.send_form import UiSendForm
from app.gui.user_address import UiUsersAddress
from app.gui.users_wallet import UiUsersWallet

from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6.QtGui import QPalette, QColor, QIcon, QTransform, QFont
from PyQt6.QtCore import Qt

from fake_useragent import UserAgent


def print_tables():
    table_users = PrettyTable()
    table_users.field_names = ['id', 'username', 'password_hash', 'salt']
    table_balances = PrettyTable()
    table_balances.field_names = ['user_id', 'currency', 'amount']
    table_addresses = PrettyTable()
    table_addresses.field_names = ['user_id', 'address']

    with sqlite3.connect('data/users.db') as db:
        cursor = db.cursor()

    cursor.execute('SELECT id, username, password_hash, salt FROM users')
    for i in cursor.fetchall():
        table_users.add_row(i)
    print(table_users)

    cursor.execute('SELECT user_id, currency, amount FROM balances')
    for i in cursor.fetchall():
        table_balances.add_row(i)
    print(table_balances)

    cursor.execute('SELECT user_id, address FROM addresses')
    for i in cursor.fetchall():
        table_addresses.add_row(i)
    print(table_addresses)


def is_password_correct(password):
    if len(password) <= 4:
        return 'Password must be longer than 4 characters'
    for i in password:
        if i.isupper():
            break
    else:
        return 'Password must contain uppercase letters'
    for i in password:
        if i.isdigit():
            break
    else:
        return 'Password must contain numbers'
    for i in password:
        if i in SPECIAL_CHARACTERS:
            break
    else:
        return 'Password must contain special characters'
    return True


def is_username_exists(username):
    with sqlite3.connect('data/users.db') as db:
        cursor = db.cursor()
        cursor.execute('''
                    SELECT 1 FROM users WHERE username = ?
                ''', (username,))
        return cursor.fetchone() is not None


def clear_tables():
    with sqlite3.connect('data/users.db') as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM users;")
        cursor.execute("DELETE FROM balances;")
        cursor.execute("DELETE FROM addresses;")
        db.commit()


def create_database():
    if not os.path.exists('data/users.db'):
        with sqlite3.connect('data/users.db') as db:
            cursor = db.cursor()

            # Создание таблиц
            cursor.execute('''
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password_hash TEXT NOT NULL,
                    salt TEXT NOT NULL
                )
            ''')

            cursor.execute('''
                CREATE TABLE balances (
                    user_id INTEGER,
                    currency TEXT NOT NULL,
                    amount REAL NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')

            cursor.execute('''
                CREATE TABLE addresses (
                    user_id INTEGER,
                    address TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')

            db.commit()


def get_balance(user_id):
    with sqlite3.connect('data/users.db') as db:
        cursor = db.cursor()
        cursor.execute('''
                    SELECT currency, amount FROM balances WHERE user_id = ?
                ''', (user_id,))
        return cursor.fetchall()


def exchange_rate():
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd",
    }

    ua = UserAgent()
    headers = {
        "User-Agent": ua.random
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return None


def get_user_id(username):
    with sqlite3.connect('data/users.db') as db:
        cursor = db.cursor()
        cursor.execute('''
                        SELECT id FROM users WHERE username = ?
                    ''', (username,))
        return cursor.fetchone()[0]


def delete_user(user_id):
    with sqlite3.connect('data/users.db') as db:
        cursor = db.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        cursor.execute('DELETE FROM balances WHERE user_id = ?', (user_id,))
        cursor.execute('DELETE FROM addresses WHERE user_id = ?', (user_id,))
        db.commit()


def add_currency(user_id, currency, amount):
    with sqlite3.connect('data/users.db') as db:
        cursor = db.cursor()
        cursor.execute('''
                    SELECT amount FROM balances WHERE user_id = ? AND currency = ?
                ''', (user_id, currency))
        result = cursor.fetchone()
        if result:
            new_amount = result[0] + amount
            cursor.execute('''
                            UPDATE balances SET amount = ? WHERE user_id = ? AND currency = ?
                        ''', (new_amount, user_id, currency))
        else:
            cursor.execute('''
                            INSERT INTO balances (user_id, currency, amount)
                            VALUES (?, ?, ?)
                        ''', (user_id, currency, amount))
        db.commit()


def subtract_currency(user_id, currency, amount):
    with sqlite3.connect('data/users.db') as db:
        cursor = db.cursor()

        cursor.execute('''
                            SELECT amount FROM balances WHERE user_id = ? AND currency = ?
                        ''', (user_id, currency))
        result = cursor.fetchone()
        new_amount = float(result[0]) - amount
        cursor.execute('''
                                    UPDATE balances SET amount = ? WHERE user_id = ? AND currency = ?
                                ''', (new_amount, user_id, currency))
        db.commit()


def get_address(user_id):
    with sqlite3.connect('data/users.db') as db:
        cursor = db.cursor()
        cursor.execute('''
                    SELECT address FROM addresses WHERE user_id = ?
                ''', (user_id,))
        result = cursor.fetchone()
        return result


def add_address(user_id):
    with sqlite3.connect('data/users.db') as db:
        cursor = db.cursor()
        address = get_address(user_id)
        if not address:
            address = secrets.token_hex(20)

            cursor.execute('SELECT user_id FROM addresses WHERE address = ?', (address,))
            while cursor.fetchone() is not None:
                address = secrets.token_hex(20)

            cursor.execute('''
                        INSERT INTO addresses (user_id, address)
                        VALUES (?, ?)
                    ''', (user_id, address))

            db.commit()
            return address
        return address[0]


class LogUsers(QMainWindow, UiRegistrationForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.colors()

        self.sign_btn.clicked.connect(self.register_user)
        self.log_btn.clicked.connect(self.log_in_user)

        self.wallets = []

    def log_in_user(self):
        username = self.username.text()
        password = self.password.text()
        if is_username_exists(username):
            with sqlite3.connect('data/users.db') as db:
                cursor = db.cursor()
                cursor.execute('''
                        SELECT password_hash, salt FROM users WHERE username = ?
                    ''', (username,))
                result = cursor.fetchone()
                password_hash, salt = result
                input_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
                if input_hash == password_hash:
                    self.result.setText('Login successful')
                    self.create_new_wallet(get_user_id(username))
                else:
                    self.result.setText('Incorrect password')
        else:
            self.result.setText('User does not exist')

    def create_new_wallet(self, user_id):
        wallet = UserWallet(user_id)
        wallet.show()
        self.wallets.append(wallet)

    def register_user(self):
        password = self.password.text()
        username = self.username.text()
        if not username:
            self.result.setText('Wrong login')
        if not is_username_exists(username):
            if is_password_correct(password) is True:
                with sqlite3.connect('data/users.db') as db:
                    cursor = db.cursor()
                    salt = os.urandom(16).hex()
                    password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
                    cursor.execute('''
                            INSERT INTO users (username, password_hash, salt)
                            VALUES (?, ?, ?)
                        ''', (username, password_hash, salt))
                    db.commit()
                self.result.setText('You have successfully registered')
            else:
                self.result.setText(is_password_correct(self.password.text()))
        else:
            self.result.setText('This login is already taken')

    def colors(self):
        palette = QPalette()

        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))  # Белый цвет

        self.label.setPalette(palette)
        self.label_2.setPalette(palette)
        self.log_btn.setPalette(palette)
        self.sign_btn.setPalette(palette)


class UserWallet(QMainWindow, UiUsersWallet):
    def __init__(self, user_id):
        super().__init__()
        self.setupUi(self)

        self.user_id = user_id
        self.address = add_address(user_id)
        self.get_addresses = []
        self.send_to_addresses = []

        self.colors()

        self.update_balance()
        self.update_btn.clicked.connect(self.update_balance)
        self.send_btn.clicked.connect(self.send)
        self.get_btn.clicked.connect(self.get)
        self.delete_btn.clicked.connect(self.delete_account)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        icon = QIcon("images/down-arrow.png")
        pixmap = icon.pixmap(64, 64)

        transform = QTransform()
        transform.rotate(180)

        rotated_pixmap = pixmap.transformed(transform)

        self.send_btn.setIcon(QIcon(rotated_pixmap))
        self.get_btn.setIcon(icon)

        self.username_login()

    def username_login(self):
        with sqlite3.connect('data/users.db') as db:
            cursor = db.cursor()

            cursor.execute('SELECT username FROM users WHERE id = ?', (self.user_id,))

            username = cursor.fetchone()[0]
        self.login.setText(username)

        font = QFont()
        font.setPointSize(24)
        font2 = QFont()
        font2.setPointSize(16)
        self.login.setFont(font)
        self.excange_rate.setFont(font2)

    def delete_account(self):
        reply = QMessageBox.question(self, 'Delete Account', 'Are you sure you want to delete your account?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            delete_user(self.user_id)
            self.close()

    def get(self):
        show_address = GetAddress(self.address)
        show_address.show()
        self.get_addresses.append(show_address)

    def send(self):
        send_to_address = SendToAddress(self.user_id, self.listWidget.selectedItems())
        send_to_address.show()
        self.send_to_addresses.append(send_to_address)

    def update_balance(self):
        balance = get_balance(self.user_id)

        balance.sort(key=lambda x: -x[1])

        self.listWidget.clear()
        for currency, amount in balance:
            self.listWidget.addItem(f'{currency}: {amount}')

        data = exchange_rate()
        if data is not None:
            rates = ''
            for i in data:
                rates += f'{i}: {data[i]["usd"]} usd\n'
            self.excange_rate.setText(rates)
        else:
            self.excange_rate.setText('Error, try again later')

    def colors(self):
        palette = QPalette()

        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))

        self.label.setPalette(palette)
        self.login.setPalette(palette)
        self.excange_rate.setPalette(palette)


class GetAddress(QMainWindow, UiUsersAddress):
    def __init__(self, address):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.setText(str(address))
        self.address = address
        self.lineEdit.setEnabled(False)

        self.pushButton.setIcon(QIcon('images/clone.png'))

        self.pushButton.clicked.connect(self.copy)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def copy(self):
        pyperclip.copy(self.address)


class SendToAddress(QMainWindow, UiSendForm):
    def __init__(self, user_id, currency):
        super().__init__()
        self.setupUi(self)
        self.user_id = user_id
        self.currency = currency

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.send_btn.clicked.connect(self.send)

    def send(self):
        if not self.currency:
            self.result.setText('Cryptocurrency not selected')
            return

        crypto, amount = self.currency[0].text().split()[0][:-1], float(self.currency[0].text().split()[-1])

        if self.amount.value() == 0.00:
            self.result.setText('Amount not selected')
            return

        if float(self.amount.value()) > amount:
            self.result.setText('Wrong amount')
            return

        with sqlite3.connect('data/users.db') as db:
            cursor = db.cursor()

            cursor.execute('''
                        SELECT user_id FROM addresses WHERE address = ?
                        ''', (self.lineEdit.text(),))
            result = cursor.fetchone()
            if result is None or result[0] == self.user_id:
                self.result.setText('Wrong address')
            else:
                add_currency(result[0], crypto, self.amount.value())
                subtract_currency(self.user_id, crypto, float(self.amount.value()))
                self.result.setText('Transaction completed')


if __name__ == '__main__':
    create_database()
    app = QApplication(sys.argv)
    log_users = LogUsers()
    log_users.show()
    sys.exit(app.exec())
