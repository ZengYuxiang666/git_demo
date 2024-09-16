#导包
from pyspark import SparkConf,SparkContext
#创建Sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
#基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)
#给spark配置解释器
import os
os.environ["PYSPARK_PYTHON"] = 'C:\python39'
#通过parallelize方法将python对象加载到spark内,准备一个rdd
rdd = sc.parallelize([1,1,4,2,2,3,4,5])

#collect方法，对rdd内容转为list输出
print(rdd.collect())

#reduce方法，对rdd进行自定义聚合
rdd.reduce(lambda a,b :a+b)

#take方法：取rdd前n个元素组成list
rdd.take(3)

#count方法：对rdd元素进行统计
r = rdd.count()
print(r)