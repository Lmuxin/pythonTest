import urllib.request
import os

def url_open(url):
        req=urllib.requesst.Request(url)
        req.add_header('User-Agent','.......')
        response=urllib.request.urlopen(url)
        html=response.read()


        print(url)
        return html
    
def get_page():
    url_open(url).decode('utf-8')
    
    a=html.find('地址')+23
    b=html.find(']',a)
    
    return html[a:b]

def find_imgs(url):
      html=url_open(url).decode('utf-8') 
      img_addrs=[]
      
      a=html.find('img src=')
      
      while a!=-1:
         b=html.find('.jpg',a,a+255)

       if b!=-1:
             img_addrs.append(html[a+9:b+4])
          else:
              b=a+9
        
           a=html.find('img src=')



       for each in img_addrs:
            print(each)

           
def save_imgs(folder,img_addrs):
       for each in img_addrs:
           filename=each.split('/')[-1]
           with opem(filename,'wb')as f;
           img=url_open(each)
           f.write(img)
           

def download(folder='ooxx',pages=10)://#下载两页图片,保存在folder文件夹
    osmkdir(folder)#创建文件夹
    os.chdir(folder)#切换到当前目录

    url='https://www.google.com.hk/search?q=%E7%A7%8B%E5%A4%A9%E5%9B%BE%E7%89%87&safe=strict&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwihq6z434DXAhVEV7wKHXZ6D4UQsAQIIw&biw=1013&bih=619#imgrc=4aUAwFEgDCG9ZM:/'

    page_num=int(get_page(url))
    for i in range(pages):
        page_num-=i
        page_url=url+'page-'+str(page_num)+'#comments'
        img_addrs=find_imgs(page_url)

        save_imgs(folder,img_addrs)

if __name__=='__main__'
     download()
