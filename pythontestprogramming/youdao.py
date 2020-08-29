import urllib.request
import urllib.parse
import json

content=input("请输入需要翻译的 内容:")

url="http://fanyi.youdao.com/?keyfrom=dict2.index"

head={}
head{'user-Agen'}="



data={}
data['type']='AUTO'
data['i']=content

data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='1508503607713'
data['sign']='6a819bf3e69cc5081e67f894f5c37657'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTION'
data['typoResult']='true'
data=urllib.parse.urlencode(data).encode('utf-8')
response=urllib.request.urlopen(url,data)

html=response.read().decode('utf-8')





target=json.loads(html)
print("翻译的结果是:%s" %  (target['translateResult'][0][0]['tgt']))

