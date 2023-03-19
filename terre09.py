import sys

# Vérifier que le nombre est positif
if len(sys.argv) != 2:
    print("Erreur : Veuillez entrer un nombre positif en argument.")
    sys.exit(1)

nombre = int(sys.argv[1])

if nombre < 0:
    print("Erreur : le nombre doit être positif.")
    sys.exit(1)

if nombre == 0:
    print("Racine carrée de 0 : 0")
else:
    x = nombre
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + nombre // x) // 2

    print(f"Racine carrée de {nombre} = {x}")