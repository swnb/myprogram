#!/usr/bin/env python
#coding=utf-8
#多线程模型服务器
import threading
from socket import *
def getmes(con):
    while 1:
        data=con.recv(1024)
        if not data:
            raise KeyboardInterrupt
        print ('\n++++++++++++++++\n'+data + "\n++++++++++++++++\n")
def sendmes(con):
    while 1:
        data=raw_input("\n++++++++++++++++\nenter your message\n-->>")
        if not data:
            raise KeyboardInterrupt
        con.send(data)
port=raw_input("enter a port\n")
s=socket()
s.bind(("127.0.0.1",int(port)))
s.listen(5)
while 1:
    con,adder=s.accept()
    con.send("let's share hand\ntell me  what do you want\n")
    a=threading.Thread(target=getmes,args=[con])
    b=threading.Thread(target=sendmes,args=[con])
    a.start()
    b.start()
    a.join()
    b.join()
    con.close()
s.close()
