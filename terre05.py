import sys

# Vérifier que deux arguments ont été passés en ligne de commande
if len(sys.argv) != 3:
    print("Erreur : Veuillez entrer deux nombres en argument.")
    sys.exit(1)

# Récupérer les deux nombres passés en argument
a = int(sys.argv[1])
b = int(sys.argv[2])

# Vérifier que le deuxième nombre n'est pas nul
if b == 0:
    print("Erreur : division par zero.")
    sys.exit(1)

# Calculer le resultat et le reste de la division
resultat = a // b
reste = a % b

# Afficher le résultat et le reste
print(f"resultat: {resultat}")
print(f"reste: {reste}")

