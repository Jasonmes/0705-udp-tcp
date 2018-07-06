# 类比udp,只不过,发送和接收之前多一步链接!!!
# 1.引入模块
import socket

# if __name__ == '__main__':
#     # 2.创建tcp类型的套接字
#     #  socket.SOCK_STREAM: 指的是tcp协议
#     tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # ***比udp多一步,建立链接: 参数为元组(ip, port)***
#     tuple1 = ('192.168.44.1', 9999)
#     #  tcp和udp最重要的不同!!!  是否创建链接
#     tcp_socket.connect(tuple1)
#     print('链接成功!!!')
#     # 3.发送数据: 不需要传递ip及port了,因为已经建立了稳定的链接
#     str1 = '我是tcp客户端, 测试内容...'
#     tcp_socket.send(str1.encode())
#     # 4.接收数据: 没有最大上线了,服务端模拟使用的是windows系统,所以转码尽量使用gbk
#     #  收到的数据就是一个字符串,二进制类型; 不在包括ip及port
#     str2 = tcp_socket.recv(1024)
#     print(tuple1, str2.decode('gbk'))
#     # 5.关闭套接字
#     tcp_socket.close()

# 第一遍
# 第一次运行时候链接了udp，refuse
# one_tcptime = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# one_tcptime.connect(('10.211.55.11', 2345))
# one_tcptime.send(input('tcp send:').encode(encoding='utf-8'))
# backstr = one_tcptime.recv(1024)
# print(backstr.decode(encoding='utf-8'))
# one_tcptime.close()

# 第二遍
# _2timesco = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# _2timesco.connect(('10.211.55.11', 2345))
# _2timesco.send(input('tcp send:').encode(encoding='utf-8'))
# backstr = _2timesco.recv(1024)
# print(backstr.decode(encoding='utf-8'))
# _2timesco.close()

# 第三遍
# _3timesoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# _3timesoc.connect(('10.211.55.11', 2345))
# _3timesoc.send(input('send tcp:').encode(encoding='utf-8'))
# backstr = _3timesoc.recv(1024)
# print(backstr.decode(encoding='utf-8'))
# _3timesoc.close()

# 第四遍
# _4timeSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# _4timeSoc.connect(('10.211.55.11', 2345))
# _4timeSoc.send(input('send tcp:').encode(encoding='utf-8'))
# backstr = _4timeSoc.recv(1024)
# print(backstr.decode(encoding='utf-8'))
# _4ti


# 第五遍
_5timesoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_5timesoc.connect(('10.211.55.11', 8081))
_5timesoc.send(input('send word:').encode(encoding='utf-8'))
print(_5timesoc.recv(1024).decode(encoding='utf-8'))
_5timesoc.close()
