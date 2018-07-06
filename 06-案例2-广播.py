# 广播就是向广播地址的某个端口发送信息,那么同一个网段的所有人的该端口,都能收到这条信息;
#   当前广播地址: 192.168.71.255
#   通用广播地址: 255.255.255.255
#       upd进行广播的时候,默认广播是关闭的,需要开启;

# 1.引模块
import socket
# # 2.创建套接字
# udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # 3.开启广播选项
# #       setsockopt: 设置socket功能选项
# #       socket.SOL_SOCKET: 当前所在的socket
# #       socket.SO_BROADCAST: 广播选项处理
# #       True/1: 开启广播(不设置默认关闭)
# udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
# # 4.发送信息
# str1 = '大家好,我是吕超...我上线了...'
# tuple1 = ('255.255.255.255', 8989)
# udp_socket.sendto(str1.encode(), tuple1)

# 第一遍
# one_timesoc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # socket.SOL_SOCKET:当前所在的soc
# # socket.SO_BROADCAST:广播选项处理
# # True/1 : 开启广播
# one_timesoc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
# one_timesoc.sendto(input('send:').encode(encoding='utf-8'), ('10.211.55.11', 8081))

# 第二遍
# two_timesoc=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# two_timesoc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
# two_timesoc.sendto(input('send:').encode(encoding='utf-8'), ('10.211.55.11', 8081))
# two_timesoc.close()
# 开启


# 第三遍
_3timesco = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
_3timesco.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
_3timesco.sendto(input('send:').encode(encoding='utf-8'), ('10.211.55.11', 8081))
_3timesco.close()