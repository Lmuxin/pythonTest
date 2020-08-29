import  urllib.request
import random
url='http://www.whatismyip.com.tw'

iplist=['182.129.241.75:9000','121.31.100.231:8123','140.255.0.147:8118']#采集ip

proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})#随机使用上面设置的代理ip和端口号


opener=urllib.request.build_opener(proxy_support)  #创建opener
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')]

urllib.request.install_opener(opener)#安装一个opener

response=urllib.request.urlopen(url)

html=response.read().decode('utf-8')
print(html)


#运行失败了
