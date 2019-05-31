import requests
from bs4 import BeautifulSoup
import  bs4

def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取网页失败")

def fillUniverLiist(ulist, html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr("td")
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def showDtata(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        list = ulist[i]
        print(tplt.format(list[0],list[1],list[2],chr(12288)))

def main():
    ulist = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html =  getHtmlText(url)
    fillUniverLiist(ulist,html)
    showDtata(ulist,120)

main()





