import socket

s = socket.socket()
print("Socket created")

s.bind(('localhost',9999)) # Binding the socket to the port

s.listen(3) # 3 clients can be connected at a time

print("Waiting for connections")

while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()
    
    print("Connected with", addr,name)
    c.send(bytes('Welcome to telusko','utf-8'))
    
    c.close()
