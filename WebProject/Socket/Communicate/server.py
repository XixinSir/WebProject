import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建SOCKET对象 面向连接的
server.bind(("127.0.0.1", 9987))  # 绑定主机名和端口号
server.listen(10)  # 设置最大连接数,超过后排队
clientsock, addr = server.accept()  # 建立与客户端的连接,返回(socket object, address info)元组对象
msg = clientsock.recv(1024)  # 接收客户端发来的消息,msg为bytes类型的数据
# clientsock.send("欢迎来到服务端".encode("utf-8"))  # python3要求发送byte类型的数据,所以将它以utf-8的形式转换为bytes类型的
while 1:

    print("1: " + msg.decode("utf-8"))  # 将bytes类型的数据转换成str字符串的数据,以utf-8的形式
    clientsock.send(input("请输入数据,将传到客户端: ").encode("utf-8"))
    time.sleep(0.1)
0
clientsock.close()

