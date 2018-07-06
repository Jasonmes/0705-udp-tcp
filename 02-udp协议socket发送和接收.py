# # 1.引入socket模块
# import socket
#
# # 2.创建套接字
# udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # 3.发送数据
# str1 = '我是udp发送方, 你好...'
# tuple1 = ('192.168.44.1', 9999)
# udp_socket.sendto(str1.encode(), tuple1)
#
# # 4.接收数据(recvfrom -- 返回值是一个元组(内容和ip及端口))
# #   返回值是一个元组, 如果我分两部分接收, 那么手动拆包(接收和发送,最大64Kb)
# #   接收数据可以阻塞代码!!!(类似: input())
#
#
# # str2, tuple2 = udp_socket.recvfrom(1024)
# # print(str2)
# # print(tuple2)
# # # Linux/mac/Unix都默认使用utf-8
# # print(str2.decode('utf-8'))
# # # windows用gbk
# # # print(str2.decode('gbk'))
#
# # 关闭套接字(以后就不能在发送和接收数据了)
# # udp_socket.close()
#
# str2, tuple3 = udp_socket.recvfrom(1024)
# print('%s (%s)' % (str2.decode('utf-8'), tuple3))

# 第一遍
# import socket
# OneTimeSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# OneTimeSocket.sendto(input("send a word:").encode(encoding='utf-8'), ('10.211.55.11', 8080))
# backString, IP_port = OneTimeSocket.recvfrom(1024)
# print(backString.decode(encoding='utf-8'))
# print(IP_port)

# 第二遍
# import socket
# TwoTimeSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# TwoTimeSocket.sendto(input("send a word:").encode(encoding='utf-8'), ('10.211.55.11', 8080))
# backString, IP_port = TwoTimeSocket.recvfrom(1024)
# print(backString.decode(encoding='utf-8'))
# print(IP_port)

# 第三遍
# import socket
# ThreeTimeSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ThreeTimeSock.sendto(input('send a word:').encode(encoding='utf-8'), ('10.211.55.11', 8080))
# BackString, IP_port = ThreeTimeSock.recvfrom(1024)
# print(BackString.decode(encoding='utf-8'), IP_port)

# 第四遍
# import socket
# FourTimeSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# FourTimeSocket.sendto(input('send a word:').encode(encoding='utf-8'), ('10.211.55.11', 8080))
# backSting, IP_port = FourTimeSocket.recvfrom(1024)
# print(backSting.decode(encoding='utf-8'), IP_port)
# FourTimeSocket.close()

# 第五遍
import socket
fivtimeSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
fivtimeSocket.sendto(input('sned a word:').encode(encoding='utf-8'), ('10.211.55.11', 8080))
backstring, IP_port =fivtimeSocket.recvfrom(1024)
print(backstring.decode(encoding='utf-8'), IP_port)
