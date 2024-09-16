#导包
from pyspark import SparkConf,SparkContext
#创建Sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
#基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)
#给spark配置解释器
import os
os.environ["PYSPARK_PYTHON"] = 'C:\python39'
#读取文件转rdd对象
rdd = sc.textFile("文件路径")
#取出一个个json字符串
rdd2 = rdd.flatMap(lambda x : x.split("|"))