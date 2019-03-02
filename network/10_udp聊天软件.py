import socket


def send_msg(udp_socket):
    """发送消息"""
    dest_ip = input("请输入对方的IP：")
    dest_port = int(input("请输入对方的端口："))
    send_data = input("请输入要发送的信息：")
    # windows下使用编码gbk，Linux/mac使用utf-8
    udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接受数据"""
    # 接收并显示
    rev_data = udp_socket.recvfrom(1024)
    # windows下使用编码gbk，Linux/mac使用utf-8
    print("%s:%s" % (str(rev_data[1]), rev_data[0].decode("gbk")))


def main():

    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定信息
    udp_socket.bind(("", 7890))

    # while循环来进行处理事情
    while True:
        # 发送数据
        send_msg(udp_socket)
        # 接收并显示
        recv_msg(udp_socket)


if __name__ == '__main__':

    main()
