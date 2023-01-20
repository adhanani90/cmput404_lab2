import socket
BYTES_TO_READ = 4096

def get(host, port):
    request_data = b"GET / HTTP/1.1\nHost:" + host.encode('utf-8') + b"\n\n"
    
    # Create a socket 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #connect the socket to the server
    s.connect((host, port))
    
    #send the request data
    s.send(request_data)
    s.shutdown(socket.SHUT_WR)

    #listen for the response
    
    response = s.recv(BYTES_TO_READ)
    
    # cannot get too many bytes toegther, so we need to loop as packet size is limited
    while len(response) > 0:
        print(response)
        response = s.recv(BYTES_TO_READ)
    
    s.close()

get('www.google.com', 80)