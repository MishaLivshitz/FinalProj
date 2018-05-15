import socket
import sys
import pickle
from Client.Controllers.conn_controller import conn_controller
from Classes import Lecturer_Class

##MAIN##
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5555)
#sock.connect(server_address)
conn_controller = conn_controller(sock, server_address)
conn_controller.start_ui()

# try:
#     # Send data
#     message = ['analyze_comments', 3012]  ## 3012 - bad rate , 639 - good rate
#     print(sys.stderr, 'sending "%s"' % message)
#     message_to_send = pickle.dumps(message)
#     sock.sendall(message_to_send)
#
#     while True:
#         data = sock.recv(128)
#         data_rec = float(pickle.loads(data, encoding="ASCII"))
#         if data_rec is not None:
#             print("Lecturer rate -", data_rec)
#
#
# finally:
#     print(sys.stderr, 'closing socket')
#     sock.close()
