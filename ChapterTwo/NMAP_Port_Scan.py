#coding: utf-8
'''
Author:
       __  _             ________
 ___ _/ /_(_)__ ____ ___/_  /_  /
/ _ `/ __/ / _ `/ -_) __// / / / 
\_,_/\__/_/\_, /\__/_/  /_/ /_/  
          /___/   
Date:20170129
Desc:NMAP端口扫描，根据输入的IP地址和端口号进行扫描
#python NMAP_Port_Scan.py -H 172.16.56.132 -P 21,22,23
[*] 172.16.56.132tcp/21 closed
[*] 172.16.56.132tcp/22 open
[*] 172.16.56.132tcp/23 closed
'''

import optparse
import nmap

def nmapscan(tgtIPaddr,tgtPort):
    nmscan = nmap.PortScanner()
    nmscan.scan(tgtIPaddr,tgtPort)
    state = nmscan[tgtIPaddr]['tcp'][int(tgtPort)]['state']
    print "[*] " + tgtIPaddr + "tcp/" + tgtPort  +" " + state


def main():
    parser = optparse.OptionParser("usage  -H <target ipaddr> -p <target port>")
    parser.add_option('-H',dest='tgtIPaddr',type='string',help='specify target ipaddr')

    parser.add_option('-P',dest='tgtPort',type='string',help='specify target port[s]')
    (options,args) = parser.parse_args()
    tgtIPaddr = options.tgtIPaddr
    '''对输入Port进行分割允许输入多个Port'''
    tgtPorts = str(options.tgtPort).split(',')
   
    if(tgtIPaddr == None) | (tgtPorts[0] == None):
        print parser.usage
        exit(0)
    for tgtPort in tgtPorts:
        nmapscan(tgtIPaddr,tgtPort)

if __name__ == '__main__':
    main()



