# # oneTime-socket
# import socket
# # 创建一个套接字
# oneTimeSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sendString = input("send a word:")
# tuple1 = ('10.211.55.11', 8080)
# oneTimeSocket.sendto(sendString.encode(encoding='utf-8'), tuple1)
# oneTimeSocket.close()


# # twoTime_socket
# import socket
# twoTimeSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# twoTimeSocket.sendto(input("send a word:").encode(encoding='utf-8'), ("10.211.55.11", 8080))
# twoTimeSocket.close()

# threeTime_socket
# import socket
# threeTimesock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# threeTimesock.sendto(input("send a word:").encode(encoding='utf-8'), ('10.211.55.11', 8080))
# threeTimesock.close()

# # 第四次
# import socket
# fourTimeSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# fourTimeSocket.sendto(input('send a word:').encode(encoding='utf-8'), ('10.211.55.11', 8080))
# fourTimeSocket.close()

