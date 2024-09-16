
func_list = {}
#路由装饰器 向列表中添加数据
def route(data):
    def func_out(func):
        #添加数据
        func_list[data] = func
        def func_inner():
            pass
        return func_inner
    return func_out

@route("/index.html")
def index():
    with open("C:\pythonProject\hh\天气.html","r",encoding="utf-8") as f :
        hh = f.read()
    return hh
@route("/center.html")
def center():
    #xxxx
    return "center"


def error():
    return "404,error"


#接口
def application(request_path):
    try:
        func = func_list[request_path]
        ret = func()
        return ret
    except:
        return error()