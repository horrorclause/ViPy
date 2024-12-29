import socket
import threading

IP = '0.0.0.0'    #Accepts connections from any address
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    print(f'[*] Listening on IP {IP}:{str(PORT)}')
    
    while True:
        # This is just to see what the accepted conenction comes in as
        print(server.accept())
        
        client, address = server.accept()
        print(f'[*] Accepted a connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client, ))
        client_handler.start()
        
        
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(4096)
        print(f'[*] Received: {request.decode('utf-8')}')
        sock.send(b'You are seen...')
        
if __name__ == '__main__':
    main()