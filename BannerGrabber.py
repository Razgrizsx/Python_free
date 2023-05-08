import socket

#192.168.0.8
#192.168.0.1

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print(s.recv(1024))

def main():
    ip = input('Enter ip: ')
    port = str(input('Enter port: '))
    banner(ip, port)

main()


