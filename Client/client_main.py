import socket
from Controllers.conn_controller import conn_controller

##MAIN##
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5555)
conn_controller = conn_controller(sock, server_address)
conn_controller.start_ui()
