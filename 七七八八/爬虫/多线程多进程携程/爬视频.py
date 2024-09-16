# https://vip.lz-cdn14.com/20230710/26512_e115eb4a/2000k/hls/e4b9459d7d9000000.ts
import requests
num = 9000000
n = 1

while True :
    try:
        url = f'https://vip.lz-cdn14.com/20230710/26512_e115eb4a/2000k/hls/e4b9459d7d{num}.ts'
        resp = requests.get(url)
        f = open(f"video/{n}.ts",mode='wb')
        f.write(resp.content)
        f.close()
        resp.close()
        n += 1
        num += 1
    except :
        print("over!!!")
        break

