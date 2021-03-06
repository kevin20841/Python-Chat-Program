import socket
import select
import sys
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# if len(sys.argv) != 3:
#    print ("Usage: script, IP address, port number")
#    exit()
 
 
 
Port = 3000 #int(sys.argv[2])
 
IP = "10.144.118.26"
Port = 8081
server.bind((IP, Port))

server.listen(100)
list_of_clients = []
def clientthread(conn, addr):
    conn.send(bytes("Welcome!", "UTF-8"))
    while True:
        try:
            message = conn.recv(2048)
            if message:
                print ("<" + addr[0] + "> " + message)
            else:
                remove(conn) 
        except:
            continue
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!= connection:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + " connected") 

    start_new_thread(clientthread,(conn,addr))    
 
conn.close()
server.close()
