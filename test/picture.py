import requests
import  os
url = "http://img.netbian.com/file/2019/0505/cb065d8cccb2a29e2281c08d1f95051a.jpg"
root = "/home/wang/图片/"
path =  root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功！")
    else:
        print("文件已经存在！")
except:
    print("爬取失败！")