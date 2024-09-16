# 登录 - 得到cookie
# 带着cookie 去请求到书架url
# 我们可以使用session进行请求 - session你可以认为是一连串请求，在这个过程中cookie不会丢失
import requests
#  要登录才能爬到的东西要用session
# 1.登录
session = requests.session()
data = {
    "loginName" : "18397881293",
    "password" : "1301556431zyxzyx"
}

url = 'https://passport.17k.com/ck/user/login'
session.post(url, data=data)

# 2.拿书架上内容
# 刚才的那个session是有cookie的
resp = session.get('https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919')
print(resp.json())