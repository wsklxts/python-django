import socket


sock=socket.socket()
sock.bind(("127.0.0.1",8808))
sock.listen(5)
print(dir(socket))


while 1:
    print("server waiting.....")
    conn,addr=sock.accept()
    data=conn.recv(1024)
    print("data",data)

    # 读取html文件
    with open("login.html","rb") as f:
        data=f.read()

    msg = '欢迎！' + "\r\n"
    conn.send((b"HTTP/232.1 200 OK\r\n\r\n %s" %data))

    conn.close()