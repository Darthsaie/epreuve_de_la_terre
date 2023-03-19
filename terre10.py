import sys

# Verifier qu'un seul argument a été passé en ligne de commande
if len(sys.argv) != 2:
    print("Erreur : Veuillez entrer un nombre en argument")
    sys.exit(1)

# Récupéré le nombre passé en argument
n = int(sys.argv[1])

# Vérifier que le nombre est strictement positif
if n < 2:
    print("Erreur : Veuillez entrer un nombre strictement positif supérieur à 1 .")
    sys.exit(1)

# Parcourir les nombres de 2 à la racine carrée de n
# Si n est divisible par l'un de ces nombres, alors il n'est pas premier
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        print(f"Non, {n} n'est pas un nombre premier.")
        break
else:
    print(f" Oui, {n} est un nombre premier.")
    