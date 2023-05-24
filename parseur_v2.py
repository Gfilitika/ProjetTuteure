#installer d'abord  pybtex sur vscode avec la commande "pip install pybtex"
import pybtex.database

# Ouvrir le fichier .bib
with (open('sca_cbc.bib', 'r') as bib_file, open('MyFile.txt', "w") as fichier_txt):
    # Charger les données bibliographiques
    bib_data = pybtex.database.parse_string(bib_file.read(), bib_format='bibtex')

# Parcourir chaque entrée bibliographique 
    for entry in bib_data.entries:
    # Extraire le titre, l'auteur et l'année de publication 
        contenu = bib_data.entries[entry].fields.items()
        personne = bib_data.entries[entry].persons.items()
        #for author in personne:
        for key, value in contenu:
            # if key == 'Title':
            #     print("\n")
            fichier_txt.write(str(key + ":" + value) + "\n")    
            #print(f"{key}: {value}")
    fichier_txt.close()
        #print( "Le fichier a été crée avec succès")  
    

### trier par article
# # Fonction de tri personnalisée
# def trier_par_type(entry):
#     return entry['ENTRYTYPE']

# # Trier les entrées par type
#     bib_data.entries.sort('Author')

# # Parcourir et afficher les entrées triées
# for entry in bib_data.entries:
#     print(entry)


# ### trier par année
# # Fonction de tri personnalisée
# def trier_par_annee(entry):
#     return int(entry['year'])

# # Trier les entrées par année
#     bib_data.entries.sort(key=trier_par_annee)

# # Parcourir et afficher les entrées triées
# # for entry in bib_data.entries:
# #     print(entry)


# ### trier par auteur
# # Fonction de tri personnalisée
# def trier_par_auteur(entry):
#     try:
#         return entry['author'].split()[0]
#     except KeyError:
#         return ''

# # Trier les entrées par auteur
# bib_data.entries.sort(key=trier_par_auteur)

# # Parcourir et afficher les entrées triées
# for entry in bib_data.entries:
#     print(entry)



    # title = bib_data.entries[entry].fields.get('title')
    # author = bib_data.entries[entry].persons.get('author')
    # year = bib_data.entries[entry].fields.get('year')
    # language = bib_data.entries[entry].fields.get('language')
    
    # Afficher les informations extraites 
    # print(f'Titre : {title}')
    # print(f'Auteur(s) : {author}')
    # print(f'Année de publication : {year}\n') 
    # print(f'Langue : {language}\n')  