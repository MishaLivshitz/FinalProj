import pickle

from UI import firstScreen
from PyQt5 import QtCore, QtGui, QtWidgets

from UI.firstScreen import Ui_MainWindow
import sys


class conn_controller:

    def __init__(self, conn, server_address):
        self.conn = conn
        self.server_address = server_address
        self.conn.connect(self.server_address)

    def start_ui(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow(self)
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    def get_institutes(self):
        # self.conn.connect(self.server_address)
        try:
            # Send data
            message = ['get_institutes']
            print(sys.stderr, 'sending "%s"' % message)
            message_to_send = pickle.dumps(message)
            self.conn.sendall(message_to_send)

            while True:
                data = self.conn.recv(128)
                data_rec = dict(pickle.loads(data, encoding="ASCII"))
                if data_rec is not None:
                    return data_rec

        finally:
            print(sys.stderr, 'closing socket')
        #  self.conn.close()

    def get_lecturers(self, ins_id):

        # self.conn.connect(self.server_address)
        try:
            # Send data
            message = ['get_lecturers', ins_id]
            print(sys.stderr, 'sending "%s"' % message)
            message_to_send = pickle.dumps(message)
            self.conn.sendall(message_to_send)

            while True:
                data = self.conn.recv(4096)
                data_rec = dict(pickle.loads(data, encoding="ASCII"))
                if data_rec is not None:
                    return data_rec
        finally:

            print(sys.stderr, 'closing socket')
            # self.conn.close()

    def get_rate(self, lec_id):

        # self.conn.connect(self.server_address)
        try:
            # Send data
            message = ['analyze_comments', lec_id]
            print(sys.stderr, 'sending "%s"' % message)
            message_to_send = pickle.dumps(message)
            self.conn.sendall(message_to_send)

            while True:
                data = self.conn.recv(128)
                data_rec = float(pickle.loads(data, encoding="ASCII"))
                if data_rec is not None:
                    return data_rec
        finally:
            print(sys.stderr, 'closing socket')
            # self.conn.close()

    def get_histogram(self, lec_id):

        # self.conn.connect(self.server_address)
        try:
            # Send data
            message = ['analyze_comments_by_period', lec_id]
            print(sys.stderr, 'sending "%s"' % message)
            message_to_send = pickle.dumps(message)
            self.conn.sendall(message_to_send)

            while True:
                data = self.conn.recv(4096)
                data_rec = dict(pickle.loads(data, encoding="ASCII"))
                if data_rec is not None:
                    return data_rec
        finally:
            print(sys.stderr, 'closing socket')
            # self.conn.close()
