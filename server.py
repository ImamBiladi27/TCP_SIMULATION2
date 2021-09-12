import socket

class Server:
    tcpServerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    Server = ("192.168.1.6",59000)
    tcpServerSocket.bind(Server)
    tcpServerSocket.listen(5)
    newSocket,clientAddress = tcpServerSocket.accept()
obj=Server()
def server():
    receiveData = obj.newSocket.recv(1024)
    print(" data yang diterima dari Client ：%s"%receiveData.decode())
    list=['SYN','ACK']
    obj.newSocket.send(list[0].encode())
    obj.newSocket.send(list[1].encode())
    receiveData = obj.newSocket.recv(1024)
    print(" data yang diterima dari CLient ：%s"%receiveData.decode())
    obj.newSocket.close()
    obj.tcpServerSocket.close()
server()