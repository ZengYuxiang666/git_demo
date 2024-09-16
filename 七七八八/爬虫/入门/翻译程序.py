import requests
url = 'https://fanyi.baidu.com/sug'
while True:
    s = input("请输入你要查的英语单词：")
    dic = {
        "kw": s
    }
    resp = requests.post(url, data=dic)
    data = resp.json()['data']
    num = 1
    for x in data :
        print(f"{num}. " + x['v'])
        num += 1
