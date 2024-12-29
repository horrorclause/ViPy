import socket

target_host = "127.0.0.1"
target_port = 9998

#Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to the client
client.connect((target_host, target_port))

#Send some data
client.send(b"GET / HTTP/1.1\r\nHost: localhost\r\nThis is my first time logging on\r\n")

#Receive some data
response=client.recv(4096)

print(response.decode())
client.close()