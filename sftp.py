__author__ = 'Administrator'
import paramiko
import re
port = 4521
ssh = paramiko.SSHClient()
t = paramiko.Transport(("120.138.75.88",port))
t.connect(username='program',password='jojwor?2343joljo')
sftp = paramiko.SFTPClient.from_transport(t)
localpath = R"D:\aa\a.txt"
remotepath = '/var/ftp/qmrserver/b.txt'
#stdin,stdout,stderr = ssh.exec_command('ls')
#print stdout.readlines()

sftp.put(localpath,remotepath)
t.close()

