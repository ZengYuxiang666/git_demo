import socket
import threading
import dynamic.frame

class Httpserver:
    def __init__(self):
        # 创建服务端对象
        self.socket_server = socket.socket()
        # 设置端口复用
        self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定ip地址和端口
        self.socket_server.bind(("0.0.0.0", 9979))#不可用local
        # 监听端口  listen方法内接收一个整数，表示接受链接的数量
        self.socket_server.listen(128)
# OKle，还有其他不明白，后期i特我即可，好
    ##　　在HTTP1.1中总共定义了8种方法：
#推荐测试工具 postman
# 　　在HTTP1.0中，定义了三种请求方法：GET,POST和HEAD方法。
#
# 　　在HTTP1.1中，新增了五种请求方法：OPTINOS,PUT,DELETE,TRACE和CONNECT方法。
    def fuc(self, conn):
        # 获取浏览器的请求信息
        client_socket_data = conn.recv(1024).decode("UTF-8")
        print(client_socket_data)
        # 判断客户端是否关闭
        if not client_socket_data:
            conn.close()
            return

        # 读取指定页面数据，将页面数据组装成HTTP响应报文发送给浏览器
        client_socket_data1 = client_socket_data.split(" ")
        request_path = client_socket_data1[1]
        if request_path == "/":
            request_path = "/天气.html"
        #服务器判断是否为动态资源
        if request_path.endswith(".html"):
            #应答行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 应答头
            response_header = "Sever:pwb\r\n"

            response_body = dynamic.frame.application(request_path)

            response_data = (response_line + response_header + "\r\n" + response_body).encode("utf-8")

            conn.send(response_data)
            conn.close()
        else:
            '''静态资源'''
            try:
                with open(request_path, "rb") as f:
                    file_data = f.read()
            except:
                # 应答行
                response_line = "HTTP/1.1 404 Not Found \r\n"
                # 应答头
                response_header = "Sever:pwb\r\n"
                # 应答体
                response_body = "Sorry, 404 Not Found,wo ai zhang jin en"

                response_data = (response_line + response_header + "\r\n" + response_body).encode()

                conn.send(response_data)

            else:
                # 应答行
                response_line = "HTTP/1.1 200 OK \r\n"
                # 应答头
                response_header = "Sever:pwb\r\n"
                # 应答体
                response_body = file_data

                response_data = (response_line + response_header + "\r\n\r\n").encode() + response_body

                conn.send(response_data)
            finally:
                conn.close()

    def start(self):
        while True:
            # accept方法返回值是二元元组（“链接对象”，客户端地址信息） accept是阻塞方法
            # 建立连接
            conn, address = self.socket_server.accept()
            # 创建子线程
            sub_thread = threading.Thread(target=self.fuc, args=(conn,))
            sub_thread.start()


# 创建服务器对象
httpserver = Httpserver()
# 启动服务器
httpserver.start()