import sys

# Vérifier qu'un seul argument a été passé en ligne de commande
if len(sys.argv) != 2:
    print("Erreur : veuillez entrer une heure en argument (format 12h).")
    sys.exit(1)

# Récupérer l'heure passée en argument
heure_12h = sys.argv[1]

# Vérifier que l'heure est au bon format (AM ou PM et un seul ":")
if not (heure_12h[-2:] == "AM" or heure_12h[-2:] == "PM") or heure_12h.count(":") != 1:
    print("Erreur : l'heure doit être au format 12h (exemple : 11:40PM).")
    sys.exit(1)

# Extraire les heures et les minutes de l'heure en format 12h
heures_12h, minutes = heure_12h[:-2].split(":")

# Vérifier que les heures et les minutes sont valides
if int(heures_12h) < 1 or int(heures_12h) > 12 or int(minutes) < 0 or int(minutes) > 59:
    print("Erreur : l'heure ou les minutes sont invalides.")
    sys.exit(1)

# Convertir l'heure en format 24h en fonction des cas AM et PM
if heures_12h == "12" and heure_12h[-2:] == "AM":
    heures_24h = "00"
elif heures_12h == "12" and heure_12h[-2:] == "PM":
    heures_24h = "12"
else:
    heures_24h = str((int(heures_12h) + 12) % 24 if heure_12h[-2:] == "PM" else int(heures_12h)).zfill(2)

# Concaténer les heures et les minutes pour former l'heure en format 24h
heure_24h = heures_24h + ":" + minutes

# Afficher l'heure en format 24h
print(heure_24h)
