import socket
import threading

BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            conn.send(data) 
        

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # setting the REUSEADDR flag meets that whilst the address is in a timeout, the socket can be reused
        
        # listening on the bound socket
        s.listen(2)
        
        conn, addr = s.accept() # returns a new socket object representing the connection and a tuple holding the address of the client
        print("Connected by", addr)
        handle_connection(conn, addr)
        
    return 

def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen()
        
        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_connection, args=(conn, addr))
            thread.run()

start_server()
#start_threaded_server()
