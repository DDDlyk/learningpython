
import socket


def main():
    # 创建一个套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    local_addr = ("", 7890)
    udp_socket.bind(local_addr)
    while True:

        # 从键盘获取数据
        send_data = input("请输入要发送的数据:")

        # 如果输入的数据是exit，那么久退出程序
        if send_data == "exit":
            break

        # 可以使用套接字收发数据
        # udp_socket.sendto("hahahah", 对方的IP以及port)
        # udp_socket.sendto("hahahah", ("192.168.1.104", 8080))
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.1.105", 8080))

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()

