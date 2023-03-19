import sys
# Vérifier qu'il y a bien trois arguments en ligne de commande
if len(sys.argv) != 4:
    print("Erreur : Veuillez  entrer trois entiers en argument.")
    sys.exit(1)

# Récupérer les entiers passés en argument
a, b, c = map(int, sys.argv[1:])

# Trouver la valeur du millieu et afficher le résultat
if a != b and a != c:
    if (a<b<c) or (c<b<a):
        print(b)
    elif (b<a<c) or (c<a<b):
        print(a)
    else:
        print(c)
else:
    print("Erreur : Les trois entiers sont identiques.")