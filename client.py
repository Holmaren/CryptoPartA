# COMP90043 Cryptography and Security Client Implementation
# University of Melbourne
# For use in Project 
# 
# Commissioned by Prof. Assoc. Udaya P.
# Authored by Renlord Y.
#
# INSTRUCTIONS TO CANDIDATES:
# Do not alter any code in here. If you break it, it will not communicate properly with the server.
# 
# 23 Jul 2015

import socket as s
import sys

from client_protocol import *
from part1_crypto import *

DEST_HOST = ''
DEST_PORT = 8001
DEBUG = True

class ClientServer:
    def __init__(self, socket, student_id):
        self.sock = socket
        self.clientProtocol = ClientProtocol(student_id)
        self.sharedKey = None

    # A Better send function for sockets with error handling
    def send(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("Socket Connection Broken")
            totalsent = totalsent + sent

        if DEBUG is True:
            print("SENT: {0}".format(self.clientProtocol.parse(msg)))

    # A Better Socket Receiver with Error Handling
    def receive(self, key=None):
        msg = self.sock.recv(4096)
        if key is not None:
            msg = decrypt(msg, key)
            print("DECRYPTED. Followed by Plain Text Message:")
        result = self.clientProtocol.parse(msg)
        if DEBUG is True:
            print("RECEIVED: " + str(result))
        return result
        
    def contact_phase(self):
        self.send(self.clientProtocol.hello())
        self.clientProtocol.counter += 1
        while True:
            msg = self.receive()
            try:
                if msg["type"] == "SERVER_HELLO":
                    return True 
                if msg["type"] == "SERVER_BUSY":
                    return False
            except KeyError:
                print("KeyError: Message does not contain all required fields")
                sys.exit(1)

    def exchange_phase(self):
        self.send(self.clientProtocol.dhex_start())
        self.clientProtocol.counter += 1
        while True:
            msg = self.receive()
            try:
                if msg["type"] == "SERVER_DHEX":    
                    self.dh_generator = int(msg["dh_g"])
                    self.dh_prime = int(msg["dh_p"])
                    self.dh_Ys = int(msg["dh_Ys"])
                    if "dh_Xc" in msg.keys():
                        self.dh_Xc = int(msg["dh_Xc"])
                        self.dh_Yc = diffie_hellman_pair(self.generator, self.dh_prime, self.dh_Xc)[1]                        
                    else:
                        self.dh_Xc = diffie_hellman_private(2048)
                        self.dh_Xc, self.dh_Yc = diffie_hellman_pair(self.dh_generator, self.dh_prime, self.dh_Xc)
                    break
            except KeyError:
                print("KeyError: Message does not contain all required fields")
                sys.exit(1)

        self.send(self.clientProtocol.dhex(self.dh_Yc))
        self.clientProtocol.counter += 1

        while True:
            msg = self.receive()
            try:
                if msg["type"] == "SERVER_DHEX_DONE":    
                    self.sharedKey = diffie_hellman_shared(self.dh_Xc, self.dh_Ys, self.dh_prime)
                    break
            except KeyError:
                print("KeyError: Message does not contain all required fields")
                sys.exit(1)

        self.send(self.clientProtocol.dhex_done())
        self.clientProtocol.counter += 1

        return True

    def exit(self):
        while True:
            msg = self.receive()
            try:
                if msg["type"] == "SERVER_FINISH":    
                    break
            except KeyError:
                print("KeyError: Message does not contain all required fields")
                sys.exit(1)
        print("Client Tasks completed successfully. Terminating cleanly...")
        self.sock.close()
        return True 

def main(student_id): 
    socket = s.socket()
    socket.connect((DEST_HOST, DEST_PORT))
    print("Connected to Server...")
    c = ClientServer(socket, student_id)
    print("==================== 1) Contact Phase Now ====================")
    c.contact_phase()
    print("==================== 2) Exchange Phase Now ===================")
    c.exchange_phase()
    c.exit()

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        print("python client.py [STUDENT_ID] [HOST?] [PORT_NO?]")
        sys.exit(1)
