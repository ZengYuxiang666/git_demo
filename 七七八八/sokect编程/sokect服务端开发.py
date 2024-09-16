import socket
#创建服务端对象
socket_server = socket.socket()
#绑定ip地址和端口
socket_server.bind(("localhost",6666))
#监听端口  listen方法内接收一个整数，表示接受链接的数量
socket_server.listen(1)

#等待客户端连接

#accept方法返回值是二元元组（“链接对象”，客户端地址信息） accept是阻塞方法
conn,address = socket_server.accept()

print(f"接收到了客户端链接，地址是{address}")

while True :
    #接收客户端信息，要使用客户端和服务器本次链接对象，而非socket对象
    #recv方法接受参数是缓冲区大小，一般给1024
    #recv返回值是字节数组，要用decode解码
    data = conn.recv(1024).decode("UTF-8")
    print(f"客户端发来的信息是{data}")

    if data == "exit" :
        break

    # 发送回复信息
    msg = input("请输入你要发送的信息：").encode("UTF-8")
    conn.send(msg)

#关闭链接
conn.close()
socket_server.close()

