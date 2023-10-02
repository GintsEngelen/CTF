import socket, sys, time

def listen(ip,port):
    pass

hostname = "mercury.picoctf.net"
port = 7449

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((hostname, port))

data = mysocket.recv(1024).decode()
data = data.split("\n")

output = ""
for entry in data:
    if entry is not '':
        output += chr(int(entry))


print(output)
