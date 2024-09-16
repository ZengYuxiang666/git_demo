import requests

num = 9000000
n = 1
url_base = f'https://vip.lz-cdn14.com/20230710/26512_e115eb4a/2000k/hls/e4b9459d7d'
url = f'{url_base}{num}.ts'

while True:
    try:
        resp = requests.get(url)
        with open(f"video/{n}.ts", mode='wb') as f:
            f.write(resp.content)
        resp.close()
        n += 1
        num += 1
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching {url}: {str(e)}")
        break