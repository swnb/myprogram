#!/usr/bin/env python
#这是非多线程的通信（c/s）模型
import socket
s=socket.socket()
s.connect(("127.0.0.1",1235))
while 1:
    print(s.recv(1024))
    s.send("i am client,let's share hands")
    data=s.recv(1024)
    if not data:
        break
    print data
    data=raw_input("i'm here to waiting for what you wanna say\n")
    if not data:
        break
    s.send(data)
s.close()
