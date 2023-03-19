import sys

# Récupérer la lettre passée en argument
lettre = sys.argv[1]

# Parcourir les lettres de l'alphabet à partir de la lettre donnée
for c in range(ord(lettre), ord('z')+1):
    print(chr(c), end='')

print()
