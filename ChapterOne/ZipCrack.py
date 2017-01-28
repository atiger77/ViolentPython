#coding: utf-8
'''
Author:
       __  _             ________
 ___ _/ /_(_)__ ____ ___/_  /_  /
/ _ `/ __/ / _ `/ -_) __// / / /
\_,_/\__/_/\_, /\__/_/  /_/ /_/
          /___/

Remark:
zip压缩加密命令 zip -r -P password zipfile.zip sourcefiles.txt
zip压缩解密命令 unzip -P password zipfile.zip -d /home/xxx
'''

import zipfile,optparse,os
from threading import Thread

#将处理语句函数化
def extractfile(zFile,password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Found Password: ' + password 
    except:
        pass

def main():
    #添加可选参数
    parser = optparse.OptionParser("Usage -f <zipfile> -d <dictionary>")    
    parser.add_option('-f',dest='zname',type='string',help='specify zip file')
    parser.add_option('-d',dest='dname',type='string',help='specify dictionary file')
    (options,args) = parser.parse_args()
    #print options.zname,options.dname
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    elif os.path.exists(options.zname) & os.path.exists(options.dname):
        zname = options.zname
        dname = options.dname
    else:
        print "[!]File not exist!"
        exit(0)
    
    zFile = zipfile.ZipFile(zname)
    passfile = open(dname)
    for line in passfile.readlines():
        password = line.strip('\n')
        #使用多线程进行破解
        t = Thread(target=extractfile,args=(zFile,password))
        t.start()
    
  
if __name__ == '__main__':
    main()
