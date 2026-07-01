import time
from pyspark.sql import SparkSession

spark=SparkSession.builder\
    .appName("timesession")\
    .getOrCreate()

df=spark.read.csv("hdfs://localhost:9000/data/raw/users.csv",
header=True,
inferSchema=True)

debut=time.time()
df.count()
fin=time.time()

print("voila les seconde",fin-debut)

