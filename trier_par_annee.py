import pybtex.database

contenu=[]
# Ouvrir le fichier .bib en lecture
with open('sca_cbc.bib', 'r') as fichier_bib:
    # Charger les données bibliographiques
    bib_data = pybtex.database.parse_string(fichier_bib.read(), bib_format='bibtex')

# Fonction de tri personnalisée
# Fonction python pour voir si la valeur est composée que de chiffres
def trier_par_annee(entry_key):
    entry = bib_data.entries[entry_key]
    year = entry.fields.get('year', '')
    if year.isdigit():
        return int(year)
    else:
        return 0

# Trier les entrées en fonction des années 
donnees_triees = sorted(bib_data.entries, key=trier_par_annee)

# Ouvrir le fichier texte en écriture
with open('annee.txt', 'w') as fichier_txt:
    # Parcourir et écrire les entrées triées dans le fichier texte
    for entry_key in donnees_triees: 
        entry = bib_data.entries[entry_key] 
        authors = entry.persons.get("author", [])      
        
    # Affichage des données  
        contenu.append("Cle d'entree: " + entry_key)

        contenu.append("Type: " + entry.type.capitalize())

        contenu.append("Champs: ")

        for field in entry.fields:     
            contenu.append("   "+ field+ ": "+ entry.fields[field])
        contenu.append("   Auteur(s): ")
        for author in authors: 
            contenu.append("             " + str(author))
        contenu.append("\n" "---" "\n")

    for element in contenu:
        fichier_txt.write(element+"\n") 
    fichier_txt.close()