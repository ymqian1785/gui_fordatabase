import paramiko
#获取SSHClient实例
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接SSH服务端
client.connect("17.131.128.5",21,username="TJOCR",password="TJOCR")
#获取Transport实例
tran = client.get_transport()
#获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)

remotepath=''
localpath=''

sftp.get(remotepath, localpath)
client.close()

# /OCR/2018/11/07/Image/TSN2014_2018110717364967835.jpg
# /OCR/2018/11/07/Head/TSN2014_2018110717364967835.jpg

# import os,sys
# import paramiko
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('172.16.0.10', 21, 'root', '123456')
#
# t = paramiko.Transport(('172.16.0.19',21))
# t.connect(username='root', password='123456')
# sftp = paramiko.SFTPClient.from_transport(t)
# sftp.get('', '')
# t.close()