import socket
# -*- coding: utf-8 -*-
__author__ = 'luoguoling'
#socket_server.py
# -*- coding: utf-8 -*-

import socket
import os
import sys
import logging
import time
import commands
import subprocess
def stopjava():

    os.system('pkill java')
def startjava():
    p = subprocess.Popen("/data/game/qmrserver1/qmrserver && /bin/sh start.sh",shell=True,close_fds=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    errorput = p.stderr.read()
    stdoutput = p.stdout.read()

def updatejava():

#    os.system('rsync -vzrtopg --progress --stats  /var/ftp/qmrserver/* /data/game/qmrserver10002/qmrserver > /dev/null 2>&1')
    r = subprocess.Popen("rsync -vzrtopg --progress --stats  /var/ftp/qmrserver/* /data/game/qmrserver1/qmrserver > /dev/null 2>&1")
    r.wait()
    errorput = r.stderr.read()
    stdoutput = r.stdout.read()

def transfertime(ret):
    a = filter(str.isdigit,ret)
    a = list(a)
    c = ''
    for i in range(len(a)):
        c += a[i]
        if i in (3,5):
            c += '-'
        if i==7:
            c += ' '
        if i in (9,11):
            c += ':'
    a = time.mktime(time.strptime(c,'%Y-%m-%d %H:%M:%S'))
    return a
def work():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	sock.bind(('49.213.70.62',1003))
#        sock.bind(('127.0.0.1',7777))
        sock.listen(5)
        while True:
                try:
                        conn, addr = sock.accept()
                        print "connection is from",conn.getpeername()
                        socketpair = conn.getpeername()
                        ip = socketpair[0]
                        print ip

                        conn.settimeout(25)
#                       logging.basicConfig(filename = os.path.join(os.getcwd(),'log.txt',level = logging.INFO,filemode = 'w')
                        ret = conn.recv(2048)
#                       logging.info(ip,ret)
                        if ip == '221.237.152.208' or ip == '221.237.152.108' or ip == '63.216.57.220' or ip == '120.138.75.88':
#			if ip == '221.237.152.108':
                            if ret == 'reboot':
				conn.sendall('已收到请求，正在处理中...')
                                stopjava()
                                time.sleep(25)
                                startjava()
                            elif ret == 'banben':
				conn.sendall('已收到请求，正在处理中...')
                                updatejava()
			    elif ret == 'time':
#				conn.sendall('已收到请求，正在处理中...')
                                shijian = os.popen('date +"%Y-%m-%d %H:%M:%S"').read()

#                                data = 'time...' + str(shijian) + '?'
                                conn.sendall(shijian)
			    elif not ret:
				print "没有数据"
				pass
                            else:
#				conn.sendall('已收到请求，正在处理中...')
				try:
					global time1
                                	time1 = transfertime(ret)
                                	timett = commands.getoutput('date "+%Y-%m-%d %H:%M:%S"')
                                	time2 = transfertime(timett)
				except Exception,e:
					print e
					pass
					conn.sendall('时间格式错误')
#                                print time1
#                                print time2
                                if int(time1) > int(time2):
                                    os.system('date -s "%s"' % ret)
				    conn.sendall('时间修改成功')
                                else:
				    conn.sendall('已收到请求，正在处理中...')
                                    stopjava()
                                    time.sleep(30)
                                    os.system('date -s "%s"' % ret)
#				    conn.sendall('时间修改成功')
#				    print "the time is %s" % ret
                                    startjava()
                                    time.sleep(20)
#                                    result = os.popen('sh /root/checkjava.sh').read()
#                                    print result
#                                    conn.sendall(result)
                        else:
#                            sys.exit(0)
			    print 'ip source is wrong'
#			    sys.exit(0)
                except KeyboardInterrupt:
                        print 'Now we will exit'
#                        sys.exit(0)
                except sock.settimeout:
                        print 'timeout'
                        pass
        sock.close()

if __name__ == '__main__':
        work()

