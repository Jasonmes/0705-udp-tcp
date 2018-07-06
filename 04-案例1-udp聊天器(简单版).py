# # 1.引入模块
# import socket
# # 2.创建套接字
# udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # 处理端口
# tuple1 = ('', 9999)
# udp_socket.bind(tuple1)
# # 确定好了给谁发
# ip = input('请输入对方的IP: ')
# # 端口号是int
# port = int(input('请输入对方的端口号(1024-65535): '))
# # 刚开始的时候写死, 全部代码测试完毕在放开
# # tuple2 = ('', 8888)
# tuple2 = (ip, port)
# # 3.循环发送和接收数据
# while True:
#     # 选择先发送,发一条,收一条;  或者跳出程序
#     flag = input('输入1就是发送并接收数据, 输入2就是退出: ')
#     # 判断:
#     if flag == '1':
#         # 数据发送
#         str1 = input('输入发送的信息: ')
#         udp_socket.sendto(str1.encode('utf-8'), tuple2)
#     elif flag == '2':
#         # 退出程序
#         print('聊天结束!')
#         break
#     else:
#         print('没有此功能!!!')
#         continue
#     # 数据接收
#     str2, tuple3 = udp_socket.recvfrom(1024)
#     # linux尽量使用utf-8, windows使用gbk
#     print(tuple3, str2.decode('utf-8'))
#     # windows系统,如果用的是讲师的网络调试助手
#     # print(tuple3, str2.decode('gbk'))
# # 4.关闭套接字
# udp_socket.close()

import socket


# # 第一遍
# udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# udp_socket.bind(('', 8005))
#
# # 对方的IP，端口
# IP = input('enter other IP:')
# port = int(input('enter a port(1024-65535):'))
# Friends_add = (IP, port)
# while True:
#     choices = input('1 is send/2 is stop--(1/2)?:')
#     if choices == '1':
#         udp_socket.sendto(input('send a word:').encode(encoding='utf-8'), Friends_add)
#     elif choices == '2':
#         break
#     else:
#         print('enter is wrong')
#         continue
#     backString, IP_port = udp_socket.recvfrom(1024)
#     print(backString.decode(encoding='utf-8'), IP_port)
# udp_socket.close()

# 第二遍
# tTimeSoc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# tTimeSoc.bind(('', 9009))
# frendsIP = input('enter his IP:')
# frendsPort = int(input('enter his port:'))
# frends_add = (frendsIP, frendsPort)
# while True:
#     choices = int(input('enter your choices:'))
#     if choices == 1:
#         tTimeSoc.sendto(input('send a word:').encode(encoding='utf-8'), frends_add)
#     elif choices == 2:
#         break
#     else:
#         print('wrong')
#         continue
#     backStr, backIP_port = tTimeSoc.recvfrom(1024)
#     print(backStr.decode(encoding='utf-8'))
# tTimeSoc.close()

#  第三遍
# _3timeSoc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# _3timeSoc.bind(('', 9001))
# othersAdd = (input('IP:'), int(input('port:')))
# while True:
#     choices = int(input('chices 1/2?:'))
#     if choices == 1:
#         _3timeSoc.sendto(input('send a word:').encode(encoding='utf-8'), othersAdd)
#     elif choices == 2:
#         break
#     else:
#         print('wrong')
#         continue
#     backStr, backPort = _3timeSoc.recvfrom(1024)
#     print(backStr.decode(encoding='utf-8'))
# _3timeSoc.close()

# 第四遍
FourTimeSoc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
FourTimeSoc.bind(('', 8003))
FriendsAdd = (input('IP:'), int(input('port:')))
while True:
    chioces = int(input('enter 1/2?:'))
    if chioces == 1:
        FourTimeSoc.sendto(input('send a word:').encode(encoding='utf-8'), FriendsAdd)
    elif chioces == 2:
        break
    else:
        print('wrong')
    ip_port = FourTimeSoc.recvfrom(1024)
    print(ip_port[0].decode(encoding='utf-8'))
FourTimeSoc.close()



