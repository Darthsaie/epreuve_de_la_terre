import sys 

# Vérifier que deux arguments on été passés en ligne de commande
if len(sys.argv) != 3:
    print("Erreur : veuillez entrer deux nombres en argument")
    sys.exit(1)

# Récupérer les deux nombres passés en argument
a = float(sys.argv[1])
b = int(sys.argv[2])

# Vérifier que l'exposant n'est pas négatif
if b < 0:
    print("Erreur : l'exposant ne peut pas être negatif.")
    sys.exit(1)

# Calculer le résultat de la puissance
resultat = a ** b

# Afficher le  resultat
print(f"Resultat : {int(resultat)}")
      
