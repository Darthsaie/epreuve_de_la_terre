import sys

# Vérifier qu'un argument a été passé en ligne de commande
if len(sys.argv) != 2:
    print("Erreur : Veuillez entrer une chaine de caractères en argument.")
    sys.exit(1)

# Récupérer la chaine de caractères passée en argument
chaine = sys.argv[1]

# Afficher l'inverse de la chaine de caractères
print(chaine[::-1])

