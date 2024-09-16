import requests
from bs4 import BeautifulSoup
import time

url = 'http://www.umeituku.com/weimeitupian/'
resp = requests.get(url)
resp.encoding = 'utf-8'
main_page = BeautifulSoup(resp.text, 'html.parser')
list_a = main_page.find('div', class_='TypeList').find_all('a')

for x in list_a:
    href = x.get('href')  # 获取子页面链接
    child_page_resp = requests.get(href)  # 请求子页面
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    child_page = BeautifulSoup(child_page_text, 'html.parser')
    p = child_page.find('p', align="center")
    img = p.find("img")
    src = img.get("src")  # 获取图片源地址

    img_resp = requests.get(src)  # 请求图片资源
    img_name = src.split("/")[-1]  # 提取图片文件名
    with open(img_name, mode="wb") as f:
        f.write(img_resp.content)  # 将图片内容写入文件

    print("over!!!", img_name)
    time.sleep(1)  # 等待一秒钟，避免给服务器带来过大的压力

print("all over!!!")
