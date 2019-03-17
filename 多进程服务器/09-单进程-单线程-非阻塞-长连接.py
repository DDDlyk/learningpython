import socket
import re


def service_clint(new_socket, request):
    """为这个客户端返回数据"""
    # 1.接收浏览器发送过来的请求，即http请求
    # GET/HTTP/1.2
    # ....
    # request = new_socket.recv(1024).decode("utf-8")
    # print(">>>"*50)
    # print(request)

    request_lines = request.splitlines()
    print("")
    print(">"*20)
    print(request_lines)

    # 'GET /index.html HTTP/1.1'
    # get post put del
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        print("*"*50, file_name)
        if file_name == "/":
            file_name = "/index.html"


    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND \r\n"
        response += "\r\n"
        response += "------file not found-----"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()

        response_body = html_content

        response_header = "HTTP/1.1 200 ok\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body

        # 将response发送给浏览器
        new_socket.send(response)
        # 将response body发送给浏览器
        # new_socket.send(html_content)

    # 关闭套接字
    # new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.绑定
    tcp_server_socket.bind(("", 7890))

    # 3.变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变为非阻塞

    client_socket_list = list()
    while True:
        # 4.等待新客户端的链接
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_sockt in client_socket_list:
            try:
                recv_data = client_sockt.recv(1024).decode("utf-8")
            except Exception as ret:
                pass
            else:
                if recv_data:
                    service_clint(client_sockt, recv_data)
                else:
                    client_sockt.close()
                    client_socket_list.remove(client_sockt)

        # 5.为这个客户端服务
        # service_clint(new_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
