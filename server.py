import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.220.1', 10000)

sock.bind(server_address)

sock.listen(1)

while True:
	print("Waiting for a connection...")
	connection, client_address = sock.accept()
	try:
		print("Connection from: " + str(client_address))
		
		while True:
			data = connection.recv(16)
			print(data)
			if(data):
				connection.sendall(data)
	finally:
		connection.close()
