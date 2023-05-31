# installer d'abord  la bibliothèque pybtex sur vscode avec la commande "pip install pybtex"
# importer la bibliothèque
import pybtex.database

contenu = []

# Ouvrir le fichier .bib
with (open('sca_cbc.bib', 'r') as fichier_bib, open('parseur.txt', "w") as fichier_txt):
    # Charger les données bibliographiques
    bib_data = pybtex.database.parse_string(fichier_bib.read(), bib_format='bibtex')

# Parcourir chaque entrée bibliographique  
    for entry_key in bib_data.entries: 
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

    
