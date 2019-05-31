import requests
def test(url):
    try:
        keyword = {'wd':'python'}
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, params=keyword)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(len(r.text))
        print(r.request.url)
        print()
        return len(r.text)
    except:
        return "爬取异常！"

urls = ["https://www.baidu.com/s"]
for url in urls:
    test(url)

