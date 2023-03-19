import sys
# Vérifier si un argument a été passé
if len(sys.argv) < 2:
    print("Tu ne me la mettras pas à l'envers.")
else:
    # Vérifier si l'argument est un entier
    if sys.argv[1].isdigit():
        nombre = int(sys.argv[1])
        if nombre % 2 == 0:
            print("pair")
        else:
            print("impair")
    else:
        print("Tu ne me la mettras pas à l'envers")

