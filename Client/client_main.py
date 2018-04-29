import socket
import sys
import pickle
from Classes import Lecturer_Class

##MAIN##
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)

sock.connect(server_address)

try:
    # Send data
    message = ['analyze_comments', 17376]
    print(sys.stderr, 'sending "%s"' % message)
    message_to_send = pickle.dumps(message)
    sock.sendall(message_to_send)

    while True:
        data = sock.recv(8192)
        data_dict = dict(pickle.loads(data, encoding="ASCII"))
        lec = Lecturer_Class.Lecturer(344, 'אבנון דן', data_dict)
        lec.analyze_comments()


finally:
    print(sys.stderr, 'closing socket')
    sock.close()
