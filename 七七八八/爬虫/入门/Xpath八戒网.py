import requests
from lxml import etree
url = 'https://www.zbj.com/fw/'
resp = requests.get(url)
html = etree.HTML(resp.text)
divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]')
for div in divs:
    price = div.xpath("./div/div/div/div[3]/div[1]/span/text()")
    title = div.xpath("./div/div/div/div[3]/div[2]/a/text()")
    com_name = div.xpath("./div/div/div/a/div[2]/div[1]/div/text()")
    for x in price :
        print(x.strip("¥"))
