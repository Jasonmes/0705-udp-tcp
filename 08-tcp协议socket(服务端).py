# 注意: 服务端和客户端有明显区别: 要把主动套接字变为被动套接字
#       (就可以接收客户端发送过来的请求了);

# 1.引模块
# import socket
# # 程序入口
# if __name__ == '__main__':
#     # 2.创建tcp类型的套接字(只能主动发起链接请求,没有办法接受别人的链接请求)
#     tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # 3.先确定好自己的端口,将来为别人提供服务;
#     tcp_socket.bind(('', 1025))
#     # 4.让自己能够接受别人发送的链接请求;(变主动套接字为被动套接字)
#     #   将来用多任务实现同一时间可以多个人链接我,那么我的上线就是128个...
#     #   现阶段,无意义; 因为是单线程,我不放开,其他人就没有办法链接
#     tcp_socket.listen(128)
#     # 死循环接收客户端发送过来的链接请求;
#     #   用以保证一个客户端断开链接,其他客户端还可以继续链接
#     while True:
#         # 4.接受客户端发送过来的链接请求
#         #   返回值是一个元组: (服务于客户端的套接字, ip和端口)
#         #   tcp_socket: 只能用来接受链接请求, 链接上一个产生一个服务于客户端的socket
#         #   service_client_socket: 用来服务客户端!!!
#         #       accept()/recvfrom()/recv(): 都有阻塞代码的功能!
#         service_client_socket, ip_port = tcp_socket.accept()
#         # 5.接收数据
#         #   客户端用Windows模拟的,所以解码用gbk
#         print(service_client_socket.recv(1024).decode('gbk'))
#         # 6.发送数据
#         service_client_socket.send('已收到!!!'.encode('utf-8'))
#         # 7.关闭服务于客户端的套接字(服务端的套接字要关闭吗??? 还要服务其他客户,所以不用关闭)
#         service_client_socket.close()
#     # 服务端套接字关闭(系统维护)
#     tcp_socket.close()

# 第一遍
# import socket
#
#
# server_side = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_side.bind(('', 2991))
# # 为什么是个经验值：128
# server_side.listen(128)
# server_client, IP_port = server_side.accept()
# while True:
#
#     a = server_client.recv(1024).decode(encoding='utf-8')
#     print(a)
#     server_client.send(input("server to client:").encode(encoding='utf-8'))
#     if a == '我走了':
#         server_client.close()
#         server_side.close()
#         break

# 第二遍
import socket
server_side = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_side.bind(('', 4509))
server_side.listen(128)
while True:
    server_client, IP_port = server_side.accept()
    print(server_client.recv(1024).decode(encoding='utf-8'))
    server_client.send(input('send to client:').encode(encoding='utf-8'))
    server_client.close()
server_side.close()
