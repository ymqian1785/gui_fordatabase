import urllib.request
from bs4 import BeautifulSoup
import re#这个库导入是为了使用正则表达式读取读取找到的内容中的数字

url='http://www.heibanke.com/lesson/crawler_ex00/'
number=['']#用于储存读到的数字

while True:
    content = urllib.request.urlopen(url+number[0])#number为字符串，number[0]为数字
    bs_obj = BeautifulSoup(content,"html.parser")#html.parser表示解析网站，不返回任何值
    number = bs_obj.h3.string#网页显示出的“你需要在网址后输入数字44513”在html的h3 tag中，number在这里读出了h3里面的内容
    number= re.findall(r'\d+',number)#读出了number里面的数字
    if not number:#必须判断页面中还有是否还有number，没有说明已经到了最后一个页面，这时应该跳出循环，打印 bs_obj.h3.string
        break
    else:
        print(number[0])
print (bs_obj.h3.string)

# import urllib.request
# import urllib.parse
#
# url='http://www.iqianyue.com/mypost'
# header={
#    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }
#
# data={'name':'fengxin','pass':'123'}
# postdata=urllib.parse.urlencode(data).encode('utf8') #进行编码
# request=urllib.request.Request(url,postdata)
# reponse=urllib.request.urlopen(request).read()

fhandle=open("./1.html","wb")
fhandle.write(reponse)
fhandle.close()
