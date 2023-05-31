# installer d'abord  la bibliothèque pybtex sur vscode avec la commande "pip install pybtex"
# importer la bibliothèque
import pybtex.database

contenu=[]

# Ouvrir le fichier .bib en lecture
with open('sca_cbc.bib', 'r') as fichier_bib:
    # Charger les données bibliographiques
    bib_data = pybtex.database.parse_string(fichier_bib.read(), bib_format='bibtex')

# Fonction pour le tri par type
def trier_par_type(entry_key):
    entry = bib_data.entries[entry_key]
    return entry.type

# Trier les entrées par ordre alphabétique du type d'article
donnees_triees = sorted(bib_data.entries, key=trier_par_type)

# Ouvrir le fichier texte en écriture
with open('type.txt', 'w') as fichier_txt:
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

