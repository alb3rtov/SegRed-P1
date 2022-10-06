#!/usr/bin/python3

import socket
 
class Netcat:
    """ Python 'netcat like' module """
    def __init__(self, ip, port):

        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length = 1024):
        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)
 
    def write(self, data):
        """ Send data """
        self.socket.send(data)
    
    def close(self):
        """ Close connection """
        self.socket.close()

nc = Netcat('127.0.0.1', 12345)

while True:
    data = nc.read()
    
    if (len(data) == 0):
        break
    
    print(data)
    nc.write(b'OK')

nc.close()
