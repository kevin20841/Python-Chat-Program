import socket
import select
import sys


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#if len(sys.argv) != 3:
#    print ("Usageage: script, IP address, port number")
#    exit()

IP = "10.144.7.93"#str(sys.argv[1])
Port = 3000#int(sys.argv[2])

while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print (message)
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
