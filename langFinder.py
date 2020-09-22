import glob 
import re 
import json 
print("===Importation du models.json===")
jsonDictionnary = open("models.json","r")
jsonContent = json.load(jsonDictionnary)
def text_finder(path):
    file = open(path)
    return file.read().decode("utf-8")


def diagnostic_langue(text):

    dictionnary = {}
    chaine_split = text.split()
    print("===Parsage du fichier d'apprentissage dans le dictionnaire===")
    for word in chaine_split:
        if word.lower() in dictionnary:
            dictionnary[word.lower()] = dictionnary[word.lower()] + 1
        else :
            dictionnary[word.lower()] = 1
    dictionnary_sorted = {}
    dictionnary_sorted = sorted([[eff,mot] for mot, eff in dictionnary.items()],reverse=True)
    verify_dictionnary = {}
    #On regarde chaque mots du texte et one le compare avec les 10 mots les plus connu de notre model 
    #si il est fait parti des mots les plus connu de notre model on ajoute un point dans la langue du mot du model 
    #et on regarde quelle langue a le plus de point
    for word in dictionnary_sorted:
        for lng in jsonContent:
            for x in range(10):
                if jsonContent[lng][x][1] == word[1]:
                    if lng in verify_dictionnary:
                        verify_dictionnary[lng] = verify_dictionnary[lng] + 1
                    else:
                        verify_dictionnary[lng] = 1
    verify_sorted = sorted([[eff,mot] for mot, eff in verify_dictionnary.items()],reverse=True)
    #print(verify_dictionnary)
    return verify_sorted[0][1]

      
 


for path in glob.glob("*/it/appr/*"):
       print(diagnostic_langue(text_finder(path)))
#print(diagnostic_langue(text_finder("corpus_multi/en/appr/2009-01-14_celex_IP-09-48.en.html")))