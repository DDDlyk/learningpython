import socket


def main():
    # 1.买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.插入手机卡（绑定本地信息）
    tcp_server_socket.bind(("", 7788))

    # 3.将手机设置为正常的响铃模式（让默认的套接字由主动变为被动 listen）
    tcp_server_socket.listen(128)

    # 这个while true循环为多个客户端服务
    while True:
        print("等待一个新的客户端的到来：")
        # 4.等待别人的电话到来（等待客户端的连接 accept）
        new_client_socket, client_addr = tcp_server_socket.accept()
        # print("-----2-----")

        print("一个新的客户端已经到来%s" % str(client_addr))

        # 这个while true循环多次为一个客户端多次服务
        while True:
            # 接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print("客户端发送过来的请求是：%s " % recv_data.decode("gbk"))

            # 如果receive解堵塞，那么有两种方式：
            # 1.客户端发送过来数据
            # 2.客户端调用close导致了这里recv解堵塞
            if  recv_data:
                # 回送一部分数据给客户端
                new_client_socket.send("嘻嘻嘻".encode("gbk"))
            else:
                break

        # 关闭套接字
        # 关闭accept返回的套接字，意味着不会再为这个客户端服务
        new_client_socket.close()
        print("已经服务器完毕。。。")

    # 如果将监听套接字关闭了，那么会导致不能再次等待新客户端的到来，及xxx.accept会失败
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
