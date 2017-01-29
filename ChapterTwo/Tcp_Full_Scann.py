#coding: utf-8
'''
Author:
       __  _             ________
 ___ _/ /_(_)__ ____ ___/_  /_  /
/ _ `/ __/ / _ `/ -_) __// / / / 
\_,_/\__/_/\_, /\__/_/  /_/ /_/  
          /___/   
Date:20170129
Desc:多线程TCP全连接扫描
'''

import optparse,socket
from socket import *

def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        print "[+]%d/tcp open" % tgtPort
        connSkt.close()
    except:
        print "[-]%d/tcp closed" % tgtPort

def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Can't resolve %s : Unknown host" %tgtHost
        return


    try:
        tgtName = gethostbyaddr(tgtIP)
        print "\n[+] Scan Result for: " + tgtName[0] 
    except:
        print "\n[+] Scan Result for: " + tgtIP
    setdefaulttimeout(1)
    for tgtPort in tgtPorts()
        print "Scanning port" + tgtPort 
        connScan(tgtHost,int(tgtPort)) 

def main():
    parser = optparse.OptionParser("usage  -H <target host> -p <target port>")
    parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')

    parser.add_option('-P',dest='tgtPort',type='int',help='specify target port')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    
    if(tgtHost == None) | (tgtPort == None):
        print parser.usage
        exit(0)
if __name__ == '__main__':
    main()



