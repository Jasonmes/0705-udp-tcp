# # 1.引入模块
# import socket
#
# # 2.创建套接字
# udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # ***: 如果作为主动接收方,那么必须先绑定自己的端口!
# # tuple1 = ('192.168.44.128', 9999)
# # tuple1 = ('127.0.0.1', 9999)
# # 本地ip/127.0.0.1/'' 都可以;  就是不能写别人的
# # tuple1 = ('', 9999)
# # udp_socket.bind(tuple1)
# udp_socket.bind('10.211.55.11', 8080)
# # 3.先接收,后发送
# str2, tuple2 = udp_socket.recvfrom(1024)
# # print(tuple2, str2.decode('utf-8'))
#
# str3 = '数据已收到...'
# # 按照收到的数据的ip及port(端口), 向他发送数据
# udp_socket.sendto(str3.encode(), tuple2)
#
# # 4.关闭套接字
# udp_socket.close()
# 主动接收方

# 第一遍
# 主动接收方
# import socketrom(1024)
# OneTimeSocket.sendto("接收到了".encode(encoding='utf-8'), IP_Port)
# OneTimeSocket.close()

# 第二遍
# import socket
# TwoTimeSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# TwoTimeSocket.bind(('', 9009))
# BackString, IP_port = TwoTimeSocket.recvfrom(1024)
# TwoTimeSocket.sendto('第二遍'.encode(encoding='utf-8'), IP_port)
# TwoTimeSocket.close()

# 第三遍
# import socket
# threeTimesocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# threeTimesocket.bind(('', 9009))
# receiveStr, recIP_port = threeTimesocket.recvfrom(1024)
# print(receiveStr.decode(encoding='utf-8'))
# threeTimesocket.sendto(input('send a word:').encode(encoding='utf-8'), ('10.211.55.11', 8080))
# threeTimesocket.close()

# 第四遍
# import socket
# fourTimeSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# fourTimeSocket.bind(('', 9000))
# receiveStr, recIp_port = fourTimeSocket.recvfrom(1024)
# print(receiveStr.decode(encoding='utf-8'))
# fourTimeSocket.sendto('收到了'.encode(encoding='utf-8'), ('10.211.55.11', 8080))
# fourTimeSocket.close()

# 第五遍
# udp主动接收方
import socket
foveTimeSocet = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
foveTimeSocet.bind(('', 8007))
recSTr, recIp_port = foveTimeSocet.recvfrom(1024)
print(recSTr.decode(encoding='utf-8'))
foveTimeSocet.sendto('收到了'.encode(encoding='utf-8'), ('10.211.55.11', 8080))
foveTimeSocet.close()
