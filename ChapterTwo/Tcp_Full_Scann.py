#coding: utf-8
'''
Author:
       __  _             ________
 ___ _/ /_(_)__ ____ ___/_  /_  /
/ _ `/ __/ / _ `/ -_) __// / / / 
\_,_/\__/_/\_, /\__/_/  /_/ /_/  
          /___/   
Date:20170129
Desc:多线程TCP全连接扫描，根据输入的IP地址和端口号进行Socket连接
#python Tcp_Full_Scann.py  -H 172.16.56.132 -P 21,22,23
[-]21/tcp closed
[-]23/tcp closed
[+]22/tcp open
[+]SSH-2.0-OpenSSH_5.3
'''

import optparse,socket
from socket import *
from threading import *
'''增加信号量防止重复输出'''
screenLock = Semaphore(value=1)
def connScan(tgtIPaddr,tgtPort):
    try:
        connSkt = socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tgtIPaddr,tgtPort))
        '''接受TCP套接字的数据'''
        results = connSkt.recv(100)
        '''加锁操作'''
        screenLock.acquire()
        print "[+]%d/tcp open" % tgtPort
        print "[+]" + str(results)
    except:
        screenLock.acquire()
        print "[-]%d/tcp closed" % tgtPort
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtIPaddr,tgtPorts):
    '''校验输入IP合法性'''
    ipcheck = tgtIPaddr.split('.')
    if len(ipcheck) == 4 and len(filter(lambda x: x >= 0 and x <= 255,map(int,filter(lambda x: x.isdigit(), ipcheck)))) == 4:
        '''设置socket超时时间'''
        setdefaulttimeout(1)
        for tgtPort in tgtPorts:
            t = Thread(target=connScan,args=(tgtIPaddr,int(tgtPort)))
            t.start()
    else:
        print "Please input correct ipaddr!\ne.g:1.2.3.4"
        exit(0)



def main():
    parser = optparse.OptionParser("usage  -H <target ipaddr> -p <target port>")
    parser.add_option('-H',dest='tgtIPaddr',type='string',help='specify target ipaddr')

    parser.add_option('-P',dest='tgtPort',type='string',help='specify target port[s]')
    (options,args) = parser.parse_args()
    tgtIPaddr = options.tgtIPaddr
    '''对输入Port进行分割允许输入多个Port'''
    tgtPort = str(options.tgtPort).split(',')
    #print tgtIPaddr,tgtPort 
   
    if(tgtIPaddr == None) | (tgtPort[0] == None):
        print parser.usage
        exit(0)
    portScan(tgtIPaddr,tgtPort)

if __name__ == '__main__':
    main()



