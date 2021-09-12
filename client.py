import socket
class Client:
    tcpClientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverAddress = ("192.168.1.6",59000)
    tcpClientSocket.connect(serverAddress)
obj=Client()
def client():
    list2=['1','2']

    for a in list2:
        if a=='1':
            input_list = input("Apa Saja :")
            obj.tcpClientSocket.send(input_list.encode("gb2312"))


            receiveData = obj.tcpClientSocket.recv(1024)
            print(" data yang diterima %s"%receiveData.decode("gb2312"))

            receiveData = obj.tcpClientSocket.recv(1024)
            print(" data yang diterima %s"%receiveData.decode("gb2312"))
        #a+=1
        else:
            input_list = input("Apa Saja :")
            obj.tcpClientSocket.send(input_list.encode("gb2312"))
    obj.tcpClientSocket.close()
client()