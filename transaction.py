import random
from datetime import datetime, timedelta

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

produits_list = ["phone", "laptop", "tv", "tablet", "watch"]
villes_list = ["Lome", "Kara", "Sokode", "Atakpame", "Dapaong"]
statuts_list = ["OK", "FAILED"]

TOTAL = 10_000_000
CHUNK = 100_000

for start in range(0, TOTAL, CHUNK):

    with open("transactions.csv", "w") as f:
        f.write("id,user_id,produit,montant,date,ville,statut\n")

        date_depart = datetime(2026, 1, 1)

        for i in range(100000):
            transaction_id = random.randint(1, 10000)
            user_id = random.randint(1, 500)
            montant = random.randint(5000, 200000)

            produit = random.choice(produits_list)
            ville = random.choice(villes_list)
            statut = random.choice(statuts_list)

            date = date_depart + timedelta(days=random.randint(0, 364))

            f.write(f"{transaction_id},{user_id},{produit},{montant},{date.strftime('%Y-%m-%d')},{ville},{statut}\n")


spark=SparkSession.builder\
    .appName("clean_transaction")\
    .getOrCreate()

df=spark.read.csv("hdfs://localhost:9000/data/raw/transaction.csv",
    header=True,
    inferSchema=True)

df_clean=df.dropna()

df_clean=df_clean.dropDuplicates()
df_clean = df_clean.filter(df_clean.montant > 0)
df_clean = df_clean.filter(df_clean.statut.isin("OK", "FAILED"))

df_clean.select(F.sum("montant").alias("chiffre_affaire")).show()
transactio=df_clean.count()
print("le nombre de transaction",transactio)

ok =df_clean.filter(df_clean.statut == "ok").count
taux_reussite=(ok/transactio)*100

top_produits = df_clean.groupBy("produit_id") \
    .agg(F.count("*").alias("nombre_ventes")) \
    .agg(F.sum("montant").alias("chiffre_affaires")) \
    .orderBy(F.desc("chiffre_affaires")) \
    .show()
 

top_produits.show(5)

df_clean.groupBy("ville") \
    .agg(F.sum("montant").alias("chiffre_affaire")) \
    .orderBy("chiffre_affaire", ascending=False) \
    .show()


    


