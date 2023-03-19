import sys

# Verrifier qu'un seul argument a été passé en ligne de commande
if len(sys.argv) != 2:
    print("Erreur : Veuillez entrer un adjectif en argument.")
    sys.exit(1)

# Récuperer l'adjectif passé en argument
adjectif = sys.argv[1]

# Afficher le message de célébration
print(f"J'ai terminé l'Epreuve de la Terre et c'était {adjectif}.")

