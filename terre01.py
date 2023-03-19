fichier_str = str(__file__)
fichier_parts = fichier_str.split("/") if "/" in fichier_str else fichier_str.split("\\")
nom_fichier = fichier_parts[-1]
print(nom_fichier)
