import socket
import sys
import mysql.connector
from Server import pre_processing
from Server import command_manager
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 5555)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(5)

cnx = mysql.connector.connect(user='root', password='misha1991',
                              host='127.0.0.1',
                              database='finalproj')
DBdata = cnx.cursor()
# pre_proc = pre_processing.Process(cnx)
# pre_proc.get_details()


while True:
    myData = " "
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print(sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            myData = [DBdata]
            if data:
                myData = myData + (pickle.loads(data, encoding="ASCII"))
                # print(sys.stderr, 'received "%s"' % data)
                manager = command_manager.c_manager()
                data_list = manager.switch_demo(myData)
                if data_list:
                    connection.sendall(data_list)
            # else:
            #     print(myData)
            #     print(sys.stderr, 'no more data from', client_address)
            #     break

    finally:
        # Clean up the connection
        connection.close()
