#coding: utf-8
'''
Author:
       __  _             ________
 ___ _/ /_(_)__ ____ ___/_  /_  /
/ _ `/ __/ / _ `/ -_) __// / / / 
\_,_/\__/_/\_, /\__/_/  /_/ /_/  
          /___/   
Date:20170127
Desc:端口检测脚本，检测目标主机是否开放常用端口
'''

import socket,os,sys

def portscan():
    port_dict = {'FTP':20,'SSH':22,'telnet':23,'smtp':25,'DNS':53,'HTTP':80,'HTTPS':443,'Mysql':3306,'Redis':6379,'Jenkins':8080,'elasticsearch':9200,'zabbix':10050,'MongoDB':27017} 
    
    for i in port_dict.keys():
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect(('127',i))    



if __name__ == '__main__':
   portscan

