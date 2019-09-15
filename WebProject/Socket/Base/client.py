import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))  # connect函数接收元组型数据
msg = client.recv(1024)  # 接收从服务器发来的消息，为bytes类型的数据，大小为1024字节的缓冲区
print(msg.decode('utf-8'))  # 我们转化为str字符串类型的数据，以utf-8的形式
client.send("客户端到此一游".encode("utf-8"))  # python3要求发送bytes类型的  所以将它转换
client.close()
