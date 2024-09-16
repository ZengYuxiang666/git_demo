import requests
url = 'https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224356374661%22}'
resp = requests.get(url)
print(resp.json())