# 线程池：一次性开辟一些线程，我们用户直接给线程池提交任务，线程任务的调度交给线程池来完成
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import requests
from lxml import etree

def down_one_page(url) :

# 拿到页面源代码
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    table = html.xpath('/html/body/div[2]/div/div/div/div[4]/div[1]/div/table/tbody')
    trs = table.xpath("./tr[position()>1]")
    for tr in trs :
        txt = tr.xpath("./td/text()")
        print(txt)

down_one_page('http://www.xinfadi.com.cn/priceDetail.html')
