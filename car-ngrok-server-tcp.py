import cv2, imutils, socket
import numpy as np
import time
import base64,threading
import socket, time
from vidstream import *

import pyfirmata, cv2 ,imutils,base64,time

def veri():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(('localhost', 9999))
	server_socket.listen(5)
	print ("Listening for client . . .")
	conn, address = server_socket.accept()
	board = pyfirmata.Arduino('COM17')
	iter8= pyfirmata.util.Iterator(board)
	iter8.start()
	print ("Connected to client at ", address)
	while True:
			gelen = conn.recv(2048).decode() 
			print(gelen)
			if gelen == "w":
				board.digital[4].write(0) 
				board.digital[5].write(1)
				board.digital[6].write(0)
				board.digital[7].write(1)
			elif gelen == "s":
				board.digital[4].write(1) 
				board.digital[5].write(0)
				board.digital[6].write(1)
				board.digital[7].write(0)
			elif gelen == "d":
				board.digital[4].write(0) 
				board.digital[5].write(0)
				board.digital[6].write(0)
				board.digital[7].write(1)
			elif gelen == "a":
				board.digital[4].write(0) 
				board.digital[5].write(1)
				board.digital[6].write(0)
				board.digital[7].write(0)
			elif gelen=="o":
				board.digital[4].write(0) 
				board.digital[5].write(0)
				board.digital[6].write(0)
				board.digital[7].write(0)
			conn.send(str.encode(str("0")))

			time.sleep(0.01)
tr1 = threading.Thread(target = veri).start()

# server = StreamingServer('localhost',8888)
# t1 = threading.Thread(target=server.start_server)
# t1.start()

