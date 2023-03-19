import sys

# Vérifier qu'un seul argument a été passé en ligne de commande
if len(sys.argv) != 2:
    print("Erreur : Veuillez entrer l'heure au format 24h (exemple : 23:59).")
    sys.exit(1)

# Récupérer l'heure passée en arugment
heure = sys.argv[1]

# Vérifier que l'heure est au format 24h
if len(heure) != 5 or not heure.replace(":", "").isdigit():
    print("Erreur : l'heure doit être au format 24h (exemple : 23:59).")
    sys.exit(1)

# Convertir l'heure en format 12
heures, minutes = heure.split(":")
heures = int(heures)
minutes = int(minutes)

if heures == 0:
    heure_12h = "12:%02dAM" % minutes
elif heures < 12:
    heure_12h = "%d:%02dAM" % (int(heures), minutes)
elif heures == 12:
    heure_12h = "12:%02dPM" % minutes
else:
    heure_12h = "%d:%02dPM" % (int(heures)-12, minutes)

# Afficher l'heure en format 12h
print(heure_12h)
