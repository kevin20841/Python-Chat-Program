import socket
import select
import sys


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#if len(sys.argv) != 3:
#    print ("Usageage: script, IP address, port number")
#    exit()

IP = "10.144.118.26"#str(sys.argv[1])
Port = 8081#int(sys.argv[2])
server.connect((IP, Port))
while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            message = str(message, "UTF-8")
            print (message)
        else:
            message = sys.stdin.readline()
            server.send(bytes(message, "UTF-8"))
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
