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
    message = ['analyze_comments', 5507]
    print(sys.stderr, 'sending "%s"' % message)
    message_to_send = pickle.dumps(message)
    sock.sendall(message_to_send)

    while True:
        data = sock.recv(2048)
        data_rec = float(pickle.loads(data, encoding="ASCII"))
        # lec = Lecturer_Class.Lecturer(344, 'אבנון דן', data_rec)
        # lec.analyze_comments()
        if not None:
            print("Lecturer rate -", data_rec)


finally:
    print(sys.stderr, 'closing socket')
    sock.close()
