import paramiko
import sys,os

host ='17.131.128.5'
user = 'TJOCR'
password='TJOCR'
remote_path='/OCR/2018/11/07/Image/TSN2014_2018110717364967835.jpg'
local_path=''

t = paramiko.Transport((host,21))
t.connect(username=user,password=password)    #连接方式也可以用key，这里只需要将password=password改为pkey=key，其余的key代码与前面的一样
sftp = paramiko.SFTPClient.from_transport(t)  #使用t的设置方式连接远程主机
sftp.get('remote_path ','local_path')        #下载文件
t.close()

# /OCR/2018/11/07/Image/TSN2014_2018110717364967835.jpg
# /OCR/2018/11/07/Head/TSN2014_2018110717364967835.jpg

