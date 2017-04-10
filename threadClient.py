#!/usr/bin/env python
#coding=utf-8
#多线程的c/s模型-客户端
import threading
from socket import *
def getm(cli):
    while 1:
    	data=cli.recv(1024)
    	if not data:
        	raise KeyboardInterrupt
    	print ("\n++++++++++++++++\n"+data+"\n++++++++++++++++\n")
def sendm(cli):
    while 1:
        data=raw_input("\n++++++++++++++++\nenter your message\n-->>")
        if not data:
            raise KeyboardInterrupt
        cli.send(data)
port=raw_input("enter your port\n")
c=socket()
c.connect(("127.0.0.1",int(port)))
c.send("hello,i am client")
a=threading.Thread(target=sendm,args=[c])
b=threading.Thread(target=getm,args=[c])
a.start()
b.start()
a.join()
b.join()
c.close()
