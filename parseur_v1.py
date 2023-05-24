#recuperer les infos du fichier bib et mettre dans un fichier txt
import re 

#recuperer les infos du fichier bib mais ne peuvent pas être réutiliser dans une autre fonction car les valeurs sont stockées nul part.
def recup(nom_fichier):    
    article_dict = {}
    # info = "" 
    #fichier_bib = open('biblio.bib','r') 
    res=""
    with open('biblio.bib', 'r') as bib:
        for line in bib.readlines()[1:-1]:
            info = re.split(r'=',line.strip())
            article_dict[info[0]] = info[1] 
        for cle, valeur in article_dict.items():
    	    res=res+(cle + ":" + valeur )   
        

#fonction pour créer un fichier texte et mettre dedans un contenu qu'on passe en paramètres
#"a" ajoute
#"w" ecrit et reefface apres
#def parseur(nom_fichier_bib,contenu):
def parseur(contenu):
    with open("MyFile.txt", "w") as fichier_txt: 
        fichier_txt.write("\n"+ contenu)
        fichier_txt.close() 
    print( "Le fichier " + nom_fichier_txt + " a été crée avec succès") 


# test
def recup_test(nom_fichier_bib, nom_fichier_txt):   
    article_dict = {}

    #ouvre le fichier .bib et lit dedans, ouvre ou créer un fichier .txt
    with ( open(nom_fichier_bib,"r") as bib, open(nom_fichier_txt, "a") as fichier_txt,):
        #lit chq ligne du fichier bib sauf la 1ère et la derniere
        for line in bib.readlines()[1:-1]:
            #creer une liste 'info' avec ['titre', 'JE SUIS LE TITRE', ..., 'Bonjour tout le monde']
            info = re.split(r'=',line.strip())
            #met dans le dictionnaire la clé et ensuite la valeur (la valeur juste apres dans la liste 'info')
            article_dict[info[0]] = info[1] 
        #pour chq clé et valeur qui sont dans le dictionnaire
        for cle, valeur in article_dict.items():
            #ecrire les clé et valeur dans le fichier .txt
            fichier_txt.write("\n"+ cle + ":" + valeur)
        print( "Le fichier " + nom_fichier_txt + " a été crée avec succès")   
    

recup_test('biblio.bib','MyFile.txt')

nom_fichier_txt="MyFile.txt"
#nom_fichier_bib='biblio.bib'

#recup(nom_fichier_bib) 




  
    