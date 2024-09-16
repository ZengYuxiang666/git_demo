import requests
proxies = {
    "https" : "https://10.50.93.177"
}
resp = requests.get('https://www.zongheng.com/',proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)