import sys

# Vérifier que l'argument a été passé en ligne de commande
if len(sys.argv) != 2:
    print("Erreur : Veuillez entrer une chaine de caractère en argument.")
    sys.exit(1)

# Récupérer la chaine de caractère passée en argument
chaine = sys.argv[1]

# Calculer le nombre de caractère dans la chaine
nb_caracteres = len(chaine)

# Afficher le nombre de caractères
print(nb_caracteres)
