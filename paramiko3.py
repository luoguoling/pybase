__author__ = 'luoguoling1'
import paramiko,sys,os
import multiprocessing
user = 'root'
def ssh_cmd(host,port,user,cmd):
    msg = '_______________result:%s__________' % host
    s = paramiko.SSHClient()
#    s.load_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')
    mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
    try:
#        s.connect(host,port,user,passwd,timeout=20)
        s.connect(host,port,user,pkey=mykey,timeout=5)
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
    f = open(r'C:\Users\Administrator\Documents\GitHub\pybase\serverlist.conf')
    list = f.readlines()
    f.close()
    for IP in list:
#        print IP
        host = IP.split()[0]
        port = int(IP.split()[1])
        user = IP.split()[2]
        passwd = IP.split()[3]
        result.append(p.apply_async(ssh_cmd,(host,port,user,cmd)))
    p.close()
    for res in result:
        res.get(timeout=12)












