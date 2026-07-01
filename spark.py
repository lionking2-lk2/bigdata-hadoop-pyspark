from pyspark.sql import SparkSession
from pyspark.sql import functions as f

spark=SparkSession.builder \
    .appName("creatsession")\
    .getOrCreate()

df=spark.read.csv("hdfs://localhost:9000/data/raw/users.csv", header=True, inferSchema=True)
df.show(20)
df.printSchema()
nb_utulisateur=df.count()
df.select(f.avg("salaire")).show()
df.select(f.min("salaire")).show()
df.orderBy("salaire",ascending=False).show(10)

print(nb_utulisateur)