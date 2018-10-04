import socket

sock = socket.socket()

sock.connect(("127.0.0.1",8808))

sock.send("aaa".encode("utf-8"))

while 1:

    data = sock.recv(1024)
    if not data:
        break
    with open("hello.html","wb") as f:
        f.write(data)




