import re
import requests


def getHtmlText(url):
    try:
        kv = {'cookie':'t=7c845627963c53ebbcae66133e528cc4; cna=u+ZZFVP4EyECAXrOvlX/FrWB', 'user-agent':'Mozilla/5.0 '}
        r = requests.get(url, headers = kv, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取网页失败！")

def parsePage(list, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'"raw_title":".*?"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(":")[1])
            list.append(price, title)
    except:
        print("分析网页失败！")

def printGoodList(list):
    tplt = "{:4}\t{:8}\t{:16}"
    count = 0
    for good in list:
        count = count + 1
        print(tplt.format(count,good(0)),good(1))

def main():
    good = "书包"
    url_start = "https://s.taobao.com/search?q="+good
    deepth = 5
    list = []
    print("{:4}\t{:8}\t{:16}".format("序号", "价格", "商品名称"))
    for i in range(deepth):
        try:
            url = url_start + '&s=' + str(44 * i)
            html = getHtmlText(url)
            parsePage(list, html)
        except:
            continue
    printGoodList(list)

main()






