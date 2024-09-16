#os.listdir 列出指定目录下的内容
#os.path.isdir 判断给定目录是否为文件夹，是返回Ture，否返回False
#os.path.exists #判断给定路径是否存在，存在返回Ture，负责返回False

import os
def func(path):
    list = []
    if os.path.exists(path):
        for x in os.listdir(path) :
            new_path = path/x
            if os.path.isdir(new_path):
                list += func(new_path)
            else:
                list.append(new_path)
        return list
    else :
        print("给定路径不存在")
        return []
