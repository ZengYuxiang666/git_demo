import socket
import threading
import sys

class Httpserver:
    def __init__(self,port):
        # 创建服务端对象
        self.socket_server = socket.socket()
        # 设置端口复用
        self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定ip地址和端口
        self.socket_server.bind(("localhost", port))
        # 监听端口  listen方法内接收一个整数，表示接受链接的数量
        self.socket_server.listen(128)

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
        ressponse_path = client_socket_data1[1]
        if ressponse_path == "/":
            ressponse_path = "./hhhh.html"
        try:
            with open(ressponse_path, "rb") as f:
                file_data = f.read()
        except:
            # 应答行
            response_line = "HTTP/1.1 404 Not Found \r\n"
            # 应答头
            response_header = "Sever:pwb\r\n"
            # 应答体
            response_body = "Sorry, 404 Not Found"

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


def main():
    if len(sys.argv) != 2 :
            print("格式错误")
            return
    if not sys.argv[1].isdigit() :
        print("格式错误")
        return
    port = sys.argv[1]

    # 创建服务器对象
    httpserver = Httpserver(port)
    # 启动服务器
    httpserver.start()
if __name__ == "__main__" :
    main()