import socket
a = socket.gethostname()  # 获得本机的主机名，返回str型数据
print(a, type(a))
b = socket.gethostbyname(a)  # 根据主机名获取ip地址，返回str型数据，也可以是网络上的域名
print(b, type(b))
c = socket.gethostbyaddr(b)  # 通过ip获得该主机的一些信息，返回tuple元组型数据
print(c, type(c))
