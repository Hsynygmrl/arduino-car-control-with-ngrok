import socket, base64,cv2
import numpy as np
import time
import keyboard,threading
from vidstream import *

def veri():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect(('2.tcp.ngrok.io',15970)) #hüsonun ipsini girceksin 9999 lu olan
    while True:
        if keyboard.is_pressed('w'):
            client_socket.send(str.encode("w")) 
        elif keyboard.is_pressed('s'):
            client_socket.send(str.encode("s"))
        elif keyboard.is_pressed('d'):
            client_socket.send(str.encode("d"))
        elif keyboard.is_pressed('a'):
            client_socket.send(str.encode("a"))
        else:
            client_socket.send(str.encode("o"))
        time.sleep(0.01)
th1 = threading.Thread(target=veri).start()


# camera_client = CameraClient('10.11.6.25',8888)  # hüsonun ipsini gireceksin 8888 li olan
# th3 = threading.Thread(target=camera_client.start_stream).start()
