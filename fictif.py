with open("users.csv", "w") as f:
    # En-tête
    f.write("id,nom,age,salaire\n")

    # Génération d'un million d'utilisateurs
    for i in range(1000000):
        age = 18 + (i % 50)
        salaire = 150000 + (i % 20) * 25000

        f.write(f"{i},user{i},{age},{salaire}\n")