import urllib.request
response=urllib.request.urlopen("https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E7%A7%8B%E5%A4%A9%E5%9B%BE%E7%89%87&hs=2&pn=1&spn=0&di=42333062530&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cl=2&lm=-1&cs=768008882%2C1947169242&os=2288202617%2C4083196379&simid=3392392845%2C416375395&adpicid=0&lpn=0&ln=30&fr=ala&fm=&sme=&cg=&bdtype=0&oriquery=%E7%A7%8B%E5%A4%A9%E5%9B%BE%E7%89%87&objurl=http%3A%2F%2Fimg.taopic.com%2Fuploads%2Fallimg%2F110817%2F2443-110QG0443119.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bpw5rtv_z%26e3Bv54AzdH3Fp7h7AzdH3Fda88abAzdH3Fbmadc_z%26e3Bip4s&gsm=0")
img=response.read()
with open ('fall.jpg','wb') as f:
    f.write(img)
