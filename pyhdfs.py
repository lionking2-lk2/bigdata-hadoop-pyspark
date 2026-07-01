from hdfs import InsecureClient
client =InsecureClient('http://localhost:9870', user='user')
compteur = 0
somme_age=0
salaire_max=0
user_max=""

with client.read('/data/raw/users.csv', encoding='utf-8')as reader:

    next (reader)
    for ligne  in reader:
        parts=ligne.strip().split(",")
        age=int(parts[2])
        somme_age +=age
        compteur += 1

        user=parts[1]
        salaire=float(parts[3])

        if salaire_max < salaire:
            salaire_max=salaire
            user_max=user

    print(compteur)
    moyenne_age=somme_age/compteur
    print(moyenne_age)
    print (" l'utulisateur qui as le plus grands salire est ",user_max)
    print (salaire_max)
