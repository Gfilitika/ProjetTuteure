from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

# Ouvrir le fichier .bib et le lire
with open('biblio.bib') as bib_file:
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    bib_database = parser.parse_file(bib_file)

# Parcourir les entrées bibliographiques
for entry in bib_database.entries:
    # Obtenir les champs de l'entrée
    title = entry['title']
    author = entry['author']
    year = entry['year']

    # Afficher les informations bibliographiques
    print(f"Titre: {title}")
    print(f"Auteur(s): {author}")
    print(f"Année de publication: {year}")