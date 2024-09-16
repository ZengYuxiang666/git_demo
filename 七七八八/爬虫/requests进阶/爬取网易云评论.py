# https://music.163.com/weapi/comment/resource/comments/get?csrf_token=ddee23adee2fe260cbece5076043befe
# https://music.163.com/weapi/comment/resource/comments/get?csrf_token=ddee23adee2fe260cbece5076043befe
# 1.找到未加密的参数
# 2。想办法把参数进行加密（必须参考网易的逻辑），params，encSecKey
# 3.请求到网易，拿到评论信息
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='