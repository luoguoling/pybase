__author__ = 'luoguoling1'
import paramiko,sys,os
import multiprocessing
def ssh_cmd(host,port,user,passwd,cmd):
    msg = '_______________result:%s________' % host
    s = paramiko.SSHClient()
#    s.load_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        s.connect(host,port,user,passwd,timeout=20)
        stdin,stdout,stderr = s.exec_command(cmd)
        print msg
        cmd_result = stdout.read(),stderr.read()
        for line in cmd_result:
            print line,
        s.close()
    except paramiko.AuthenticationException:
        print msg
        print 'Authentication fail'
    except paramiko.BadHostKeyException:
        print msg
        print 'Bad host key'
if __name__ == '__main__':
    result = []
    p = multiprocessing.Pool(processes=20)
    cmd = raw_input('cmd:>')
    f = open('serverlist.conf')
    list = f.readlines()
    f.close()
    for IP in list:
#        print IP
        host = IP.split()[0]
        port = int(IP.split()[1])
        user = IP.split()[2]
        passwd = IP.split()[3]
        print host,port,user,passwd
        result.append(p.apply_async(ssh_cmd,(host,port,user,passwd,cmd)))
        p.close()
    for res in result:
        res.get(timeout=12)












