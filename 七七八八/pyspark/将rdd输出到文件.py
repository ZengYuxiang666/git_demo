#首先先下载hadoop（未完成）
#导包
from pyspark import SparkConf,SparkContext
#创建Sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
#基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)
#给spark配置解释器
import os
os.environ["PYSPARK_PYTHON"] = 'C:\python39'
#给hadoop设置环境变量
os.environ["HADOOP_HOME"] = "......."
#通过parallelize方法将python对象加载到spark内,准备一个rdd
rdd = sc.parallelize([1,1,4,2,2,3,4,5])
#输出到文件中，输出的结果是一个文件夹，有多少个分区就输出多少文件
rdd.saveAsTextFile("....")


#如何修改rdd分区
#1.Sparkconf对象设置conf.set("spark.default.parallelism","1")
#2.创建rdd时，sc.parallelize方法传入numSlices参数为1