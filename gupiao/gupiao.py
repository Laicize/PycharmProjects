import re
import requests
import traceback
from bs4 import BeautifulSoup

def getHtmlText(url):
    try:
        r = requests.get(url)
        r.status_code
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("获取页面失败！")


def getStockList(list, stockURL):
    html = getHtmlText(stockURL)
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            list.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue


def getStockInfo(list, stockURL,fpath):
    count = 0
    for stock in list:
        url = stockURL + stock + ".html"
        html = getHtmlText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, "html.parser")
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})
            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                value = valueList[i].text
                infoDict[key] = value

            with open (fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print('\r当前速度：{:.2f}%'.format(count*100/len(list),end=''))

        except:
            traceback.print_exc()

def main ():
    stock_list_url = "http://quote.eastmoney.com/stock_list.html"
    stock_info_url = "http://gupiao.baidu.com/stock/"
    output_file = "/home/wang/PycharmProjects/gupiao/gupiao.txt"
    list = []
    getStockList(list, stock_list_url)
    getStockInfo(list, stock_info_url, output_file)



main()

