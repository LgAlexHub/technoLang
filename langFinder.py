import glob 
import re 
import json 

jsonDictionnary = open("models.json","r")
jsonContent = json.load(jsonDictionnary)
def text_finder(path):
    file = open(path)
    return file.read().encode('utf-8')


def diagnostic_langue(text):
    print(text)
    dictionnary = {}
    chaine_split = text.split()
    for word in chaine_split:
        if word.lower() in dictionnary:
            dictionnary[word.lower()] = dictionnary[word.lower()] + 1
        else :
            dictionnary[word.lower()] = 1
    dictionnary_sorted = {}
    dictionnary_sorted = sorted([[eff,mot] for mot, eff in dictionnary.items()],reverse=True)
    #print(dictionnary_sorted)
    verify_dictionnary = {}
    for x in range(20):
        for lng in jsonContent:
            for word in jsonContent[lng]:
                if word[1] in dictionnary_sorted[x][1]:
                    if lng in verify_dictionnary:
                        verify_dictionnary[lng] = verify_dictionnary[lng] + 1
                    else : 
                        verify_dictionnary[lng] = 1
    verify_sorted = sorted([[eff,mot] for mot, eff in verify_dictionnary.items()],reverse=True)
    return verify_sorted[0][1]



print(diagnostic_langue(text_finder("corpus_multi/fr/appr/2009-01-19_celex_IP-09-67.fr.html")))

