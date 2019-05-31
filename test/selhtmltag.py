import requests
from bs4 import BeautifulSoup

def html():
    url = "http://python123.io/ws/demo.html"
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        soup = BeautifulSoup(demo, "html.parser")
        for link in soup.find_all('a'):
            print(link.get('href'))
    except:
        print("提取html中链接失败！")

html()



