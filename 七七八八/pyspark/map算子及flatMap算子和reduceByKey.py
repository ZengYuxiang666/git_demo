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
rdd = sc.parallelize([1,2,3,4,5])
#使用map算子（方法）：相当于遍历列表,然后对每个元素进行一次函数的操作   “及链式调用”
rdd1 = rdd.map(lambda x : x**3).map(lambda x : x+88)
print(rdd1.collect())

#flatMap的作用和map的作用差不多，只是将结果解除嵌套


#reduceByKey方法：将Key相同的数据进行函数内的操作
rdd2 = sc.parallelize([("男",99),("女",88),("男",50),("女",77)])
rdd3 = rdd2.reduceByKey(lambda x,y : x + y)
print(rdd3.collect())