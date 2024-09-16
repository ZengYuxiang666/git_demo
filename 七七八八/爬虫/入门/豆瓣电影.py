import requests
url = 'https://movie.douban.com/j/search_subjects'
param = {
    "type": "movie",
    "tag": "豆瓣高分",
    "page_limit": 50,
    "page_start": 0
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
}
resp = requests.get(url=url,params=param,headers=headers)
data = resp.json()['subjects']
for x in data :
    print(f"电影：{x['title']} \t\t评分：{x['rate']}")
resp.close()