import time
from pyspark.sql import SparkSession


with open("users_10m.csv", "w") as f:
    # En-tête
    f.write("id,nom,age,salaire\n")

    # Génération d'un million d'utilisateurs
    for i in range(10000000):
        age = 180 + (i % 500)
        salaire = 1500000 + (i % 20) * 250000

        f.write(f"{i},user{i},{age},{salaire}\n")

spark=SparkSession.builder\
    .appName("timesession")\
    .getOrCreate()

df=spark.read.csv("hdfs://localhost:9000/data/raw/users.csv",
header=True,
inferSchema=True)


debut=time.time
df.count()
fin=time.time
print("temps en seconde ",fin-debut)