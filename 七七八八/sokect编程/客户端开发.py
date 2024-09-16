import socket
#创建socket对象
socket_cilent = socket.socket()
#连接到服务端
socket_cilent.connect(("localhost",6666))
while True :
     #发送消息
     msg = input("请输入你的信息")
     if msg =="exit" :
         break
     socket_cilent.send(msg.encode("UTF-8"))
     # 接收返回消息
     recv_data = socket_cilent.recv(1024)
     print(f"服务端发来的信息是{recv_data}")
#关闭连接
socket_cilent.close()
