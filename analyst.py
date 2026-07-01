import random
from datetime import datetime, timedelta

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


#  GENERATION DU FICHIER CSV LOCAL


with open("ventes.csv", "w") as f:
    f.write("client_id,produit_id,montant,date\n")

    date_depart = datetime(2026, 1, 1)

    for i in range(100000):
        client_id = random.randint(1, 10000)
        produit_id = random.randint(1, 500)
        montant = random.randint(5000, 200000)

        date = date_depart + timedelta(days=random.randint(0, 364))

        f.write(f"{client_id},{produit_id},{montant},{date.strftime('%Y-%m-%d')}\n")

#  SPARK SESSION

spark = SparkSession.builder \
    .appName("AnalyseVentes") \
    .getOrCreate()



# LECTURE DEPUIS HDFS


df = spark.read.csv(
    "hdfs://localhost:9000/data/raw/ventes.csv",
    header=True,
    inferSchema=True
)



# ANALYSES


# Chiffre d'affaires total
ca_total = df.select(F.sum("montant").alias("chiffre_affaire_total"))

# Chiffre d'affaires par jour
ca_jour = df.groupBy("date") \
    .agg(F.sum("montant").alias("chiffre_affaire_jour")) \
    .orderBy("date")

# Chiffre d'affaires par mois
df = df.withColumn("mois", F.month("date"))

ca_mois = df.groupBy("mois") \
    .agg(F.sum("montant").alias("chiffre_affaire_mois")) \
    .orderBy("mois")

# Top 10 montants
top_ventes = df.orderBy("montant", ascending=False).limit(10)

# Top 10 produits les plus vendus
top_produits = df.groupBy("produit_id") \
    .agg(F.count("*").alias("nombre_ventes")) \
    .orderBy("nombre_ventes", ascending=False) \
    .limit(10)



# EXPORT VERS HDFS


ca_total.write.mode("overwrite") \
    .csv("hdfs://localhost:9000/data/results/ca_total", header=True)

ca_jour.write.mode("overwrite") \
    .csv("hdfs://localhost:9000/data/results/ca_par_jour", header=True)

ca_mois.write.mode("overwrite") \
    .csv("hdfs://localhost:9000/data/results/ca_par_mois", header=True)

top_ventes.write.mode("overwrite") \
    .csv("hdfs://localhost:9000/data/results/top_ventes", header=True)

top_produits.write.mode("overwrite") \
    .csv("hdfs://localhost:9000/data/results/top_produits", header=True)


# AFFICHAGE RAPIDE 


ca_total.show()
ca_jour.show(5)
ca_mois.show()
top_ventes.show(10)
top_produits.show(10)