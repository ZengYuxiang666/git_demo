# https://video.pearvideo.com/mp4/third/20231126/1701165712121-11721137-010847-hd.mp4
# https://video .pearvideo.com/mp4/third/20231126/cont-1789736-11721137-010847-hd.mp4
# 1.拿到contid
# 2.拿到videoStatus返回的json. 进一步拿到srlURL
# 3.srcURL里面的内容进行修整
# 4.下载视频
import requests

url = "https://www.pearvideo.com/video_1789736"
contid = url.split('_')[1]
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    # 防盗链   溯源
     "Referer" : url
}
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contid}&mrd=0.7955481659790615"
resp = requests.get(videoStatusUrl,headers=headers)
srcUrl = resp.json()['videoInfo']['videos']['srcUrl']
systemTime = resp.json()['systemTime']
srcUrl = srcUrl.replace(systemTime,f"cont-{contid}")
with open('视频',mode='wb') as f :
    f.write(requests.get(srcUrl).content)

# https://video.pearvideo.com/mp4/third/20231126/1701247868816-11721137-010847-hd.mp4
# https://video.pearvideo.com/mp4/third/20231126/cont-1789736-11721137-010847-hd.mp4
