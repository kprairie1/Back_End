from devices import *
import socket
import sys

def deviceFunctions(command):
	switch = {
	0: "zero", 
	1: "one", 
	2: "two", 
	}
	return switch.get(command, "nothing")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
serverAddress = (host, 10000)

print("Starting up on port: " + str(serverAddress[1]))
sock.bind(serverAddress)
sock.listen(1)

while True:
	print("Waiting for a Connection...")
	connection, clientAddress = sock.accept()
	
	try:
		print("Client Connected: " + str(clientAddress))
		while True:
			command = connection.recv(16)
			command = int(command)
			deviceFunctions(command)
			connection.sendall("Command Complete!\nPlease enter a new command")
	
	finally:
		sock.close()
