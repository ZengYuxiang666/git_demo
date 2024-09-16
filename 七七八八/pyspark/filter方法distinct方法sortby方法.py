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


#使用filter方法：相当于筛选，满足条件的会被保留
rdd1 = rdd.filter(lambda num : num % 2 ==0)

#使用distinct方法对数据进行去重（无需传参）
rdd2 = rdd.distinct()

#使用sortby方法对rdd数据进行排序  函数是排序依据，ascending决定顺序，numPartitions(int)用int区进行排序
rdd3 = rdd.sortBy(lambda x : x,ascending=True,numPartitions=1)
