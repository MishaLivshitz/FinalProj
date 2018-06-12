import pickle

from PyQt5 import QtCore, QtGui, QtWidgets

from UI.mainScreen import Ui_MainWindow
import sys

from UI.table import table_ui


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

    def show_table_ui(self):
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = table_ui(self)
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())

    def get_institutes(self):

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

        try:
            # Send data
            message = ['get_lecturers', ins_id]
            print(sys.stderr, 'sending "%s"' % message)
            message_to_send = pickle.dumps(message)
            self.conn.sendall(message_to_send)

            while True:
                data = self.conn.recv(16384)
                data_rec = dict(pickle.loads(data, encoding="ASCII"))
                if data_rec is not None:
                    return data_rec
        finally:

            print(sys.stderr, 'closing socket')
            # self.conn.close()

    def get_lecturers_table(self, ins_id):

        try:
            # Send data
            message = ['get_lecturers_table', ins_id]
            print(sys.stderr, 'sending "%s"' % message)
            message_to_send = pickle.dumps(message)
            self.conn.sendall(message_to_send)

            while True:
                data = self.conn.recv(65536)
                data_rec = list(pickle.loads(data, encoding="ASCII"))
                if data_rec is not None:
                    return data_rec
        finally:

            print(sys.stderr, 'closing socket')
            # self.conn.close()

    def get_rate(self, lec_id):

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

    def get_by_dep(self, ins_id):

        try:
            # Send data
            message = ['analyze_comments_by_department', ins_id]
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


    def get_histogram_by_ins(self, ins_id):

        try:
            # Send data
            message = ['analyze_ins_comments_by_period', ins_id]
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