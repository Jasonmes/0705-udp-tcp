# 1.引入模块
# import socket
#
#
# def send_msg(udp_socket, friendsadd):
#     udp_socket.sendto(input('输入发送的信息: ').encode('utf-8'), friendsadd)
#
#
# def receive_msg(udp_socket):
#     back = udp_socket.recvfrom(1024)
#     # linux尽量使用utf-8, windows使用gbk
#     print(back[0].decode('utf-8'))
#     # windows系统,如果用的是讲师的网络调试助手
#     # print(tuple3, str2.decode('gbk'))
#
#
# def main():
#     # 2.创建套接字
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     # 处理端口
#     udp_socket.bind(('', 9999))
#     friendsAdd = (input('请输入对方的IP: '), int(input('请输入对方的端口号(1024-65535): ')))
#     while True:
#         flag = int(input('输入1就是发送并接收数据, 输入2就是退出: '))
#         # 判断:
#         if flag == 1:
#             send_msg(udp_socket, friendsAdd)
#         elif flag == 2:
#             print('聊天结束!')
#             break
#         else:
#             print('没有此功能!!!')
#             continue
#         receive_msg(udp_socket)
#     udp_socket.close()
#
#
# if __name__ == '__main__':
#     main()


import socket


# 第一遍
# def sendto(oneudpso, friendsadd):
#     oneudpso.sendto(input('send a word:').encode(encoding='utf-8'), friendsadd)
#
#
# def receivefrom(oneudpso):
#     back = oneudpso.recvfrom(1024)
#     print(back[0].decode(encoding='utf-8'))
#
#
# def main():
#     one_udpso = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     one_udpso.bind(('', 9910))
#     friends_add = (input('IP:'), int(input('port:')))
#     while True:
#         chioces = int(input('enter 1/2?:'))
#         if chioces == 1:
#             sendto(one_udpso, friends_add)
#         elif chioces == 2:
#             break
#         else:
#             print('wrong')
#         receivefrom(one_udpso)
#     one_udpso.close()
#
#
# if __name__ == '__main__':
#     main()

# 第二遍
# def sendto(two_timesoc, friendsadd):
#     two_timesoc.sendto(input('send a word:').encode(encoding='utf-8'), friendsadd)
#
#
# def receive(two_timesoc):
#     backdata = two_timesoc.recvfrom(1024)
#     print(backdata[0].decode(encoding='utf-8'))
#
#
# def main():
#     two_timesoc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     two_timesoc.bind(('', 2345))
#     friendsadd = (input('IP:'), int(input('port:')))
#     while True:
#         chioces = int(input('enter 1/2?:'))
#         if chioces == 1:
#             sendto(two_timesoc, friendsadd)
#         elif chioces == 2:
#             break
#         else:
#             print('wrong')
#         receive(two_timesoc)
#     two_timesoc.close()
#
#
# if __name__ == '__main__':
#     main()

# 第三遍
def sendto(_3timesocke, friendsadd):
    _3timesocke.sendto(input('send a word:').encode(encoding='utf-8'), friendsadd)


def receive(_3timesocke):
    backdata = _3timesocke.recvfrom(1024)
    print(backdata[0].decode(encoding='utf-8'))

def main():
    _3timesocke = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    _3timesocke.bind(('', 4321))
    friendsadd = (input('IP:'), int(input('port:')))
    while True:
        choices = int(input('enter 1/2?:'))
        if choices == 1:
            sendto(_3timesocke, friendsadd)
        elif choices == 2:
            break
        else:
            print('wrong')
        receive(_3timesocke)
        _3timesocke.close()


if __name__ == '__main__':
    main()
