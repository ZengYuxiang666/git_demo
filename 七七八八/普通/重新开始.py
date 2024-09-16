from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
data = [("北京市",198)]
map.add("地图",data,"china")
map.set_global_opts(visualmap_opts=VisualMapOpts(is_show=True,is_piecewise=True,
pieces=[{"min":1,"max":500,"label":"1-500","color":"#FF6666"}]))
map.render()

my_list =[(99,"hh"),(88,"jj"),(77,"kk")]
def list_soft(x):
    return x[0]
my_list.sort(key=list_soft,reverse=False)
print(my_list)

class students :
    def __init__(self,name,age,ad):
        self.name = name
        self.age = age
        self.ad = ad
        print(f"学生{x}的数据录入完成，信息为{self.name,self.age,self.ad}")
for x in range(1,11) :
    print(f"当前录入第{x}位同学的信息，总共需录入10名")
    stu = students(input("请输入学生姓名："),input("请输入学生年龄："),input("请输入学生地址："))