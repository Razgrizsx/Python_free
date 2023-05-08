import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input('Enter ip to scan: ')
port = int(input('Enter port to scan: '))

def portScanner(port):
    if s.connect_ex((host, port)):
        print('Port closed')
    else:
        print('Port open')

portScanner(port)