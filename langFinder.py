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
    #print("===Parsage du fichier d'apprentissage dans le dictionnaire===")
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

      
def __precision():
    test_dictionnary={}
    for path in glob.glob("corpus_multi/*/appr/*"):
        _,lang,corpus,filename = re.split("/",path)
        #print(path)
        res = diagnostic_langue(text_finder(path))
        if lang not in test_dictionnary:
            test_dictionnary[lang]={}
            test_dictionnary[lang]["vraiPositif"]=0
            test_dictionnary[lang]["vraiNegatif"]=0
        if lang == res : 
            test_dictionnary[lang]["vraiPositif"]=test_dictionnary[lang]["vraiPositif"]+1
        else :
             test_dictionnary[lang]["vraiNegatif"]=test_dictionnary[lang]["vraiNegatif"]+1
    
    print(json.dumps(test_dictionnary,indent=2,ensure_ascii=False))         

    
       
        
def diagnostic_langue_str(text,N=3):
    
    
        

#On essaye avec tout les documents d'une langue

#a executer pour avoir une trace des touts les vrais positif et negatif du corpus 
__precision()

#a lancer pour voir le resultat d'un seul fichier
#print(diagnostic_langue(text_finder("corpus_multi/en/appr/2009-01-14_celex_IP-09-48.en.html")))