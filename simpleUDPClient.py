import socket

targetHost = "127.0.0.1"
targetPort = 57000

# Create a socket object, use DGRAM for datagram (UDP)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data
client.sendto(b'AAAAAABBBBBCCCCCCC', (targetHost, targetPort))

# Receive some data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()