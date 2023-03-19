import sys
def is_sorted(numbers):
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers) - 1))

# Vérifier qu'au moins un argument a été passé en ligne de commande
if len(sys.argv) <2:
    print("Erreur : Veuilleuez entrer une liste d'entiers en argument.")
    sys.exit(1)

try:
    # Récuperer les entiers passés en argument
    entiers = list(map(int, sys.argv[1:]))

    # Vérifier si la liste est triée et afficher le résultat
    if is_sorted(entiers):
        print("Triée !")
    else:
        print("Pas triée !")

except ValueError:
    print("Erreur : TOus les arguments doivent être des entiers.")
    
     