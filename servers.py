 #!/usr/bin/env python
#coding=utf-8
#这是非多线程的通信模型 服务器；
from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1",1234))
s.listen(5)
while 1:
    print "you are connecting"
    conn,addr=s.accept()
    conn.send("i have recvice you letter,please tell me what do you want?\n")
    while 1:
        data=conn.recv(1024)
        if not data:
            break
        print(data)
        data=raw_input("enter your word\n")
        if not data:
            break
        conn.send(data)
    conn.close()
s.close()
