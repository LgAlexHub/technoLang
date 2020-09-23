import glob 
import re 
import json 
import sys

def JsonOpenner(N):
    jsonContent = open("ModelsGrams/modelsN"+str(N)+".json","r")
    jsonReturn = json.load(jsonContent)
    jsonContent.close()
    return jsonReturn


jsonDictionnary = JsonOpenner(1)



def diagnostic_langue_str(text,N):
    jsonDictionnary = JsonOpenner(N)
    dictionnary = {}
    tableau_mot=[]
    for x in range(len(text)-N):
        tableau_mot.append(text[x:x+N])
    for word in tableau_mot:
        if word.lower() in dictionnary:
            dictionnary[word.lower()] = dictionnary[word.lower()] + 1
        else :
            dictionnary[word.lower()] = 1
    dictionnary_sorted = {}
    dictionnary_sorted = sorted([[eff,mot] for mot, eff in dictionnary.items()],reverse=True)
    verify_dictionnary = {}
    for word in dictionnary_sorted:
        for lng in jsonDictionnary:
            for x in range(10):
                if jsonDictionnary[lng][x][1] == word[1]:
                    if lng in verify_dictionnary:
                        verify_dictionnary[lng] = verify_dictionnary[lng] + 1
                    else:
                        verify_dictionnary[lng] = 1
    verify_sorted = sorted([[eff,mot] for mot, eff in verify_dictionnary.items()],reverse=True)

    return verify_sorted[0][1]

def text_finder(path):
    file = open(path)
    return file.read().decode("utf-8")

def __precision(N):
    test_dictionnary={}
    for path in glob.glob("corpus_multi/*/test/*"):
        _,lang,corpus,filename = re.split("/",path)
        #print(path)
        res = diagnostic_langue_str(text_finder(path),N)
        if lang not in test_dictionnary:
            test_dictionnary[lang]={}
            test_dictionnary[lang]["vraiPositif"]=0
            test_dictionnary[lang]["fauxNegatif"]=0
        if lang == res : 
            test_dictionnary[lang]["vraiPositif"]=test_dictionnary[lang]["vraiPositif"]+1
        else :
             test_dictionnary[lang]["fauxNegatif"]=test_dictionnary[lang]["fauxNegatif"]+1
    print(json.dumps(test_dictionnary,indent=2,ensure_ascii=False))    
    for lng in test_dictionnary:
        print(lng," rappel : ",(float(test_dictionnary[lng]["vraiPositif"])/(float(test_dictionnary[lng]["vraiPositif"])+float(test_dictionnary[lng]["fauxNegatif"]))))

__precision(int(sys.argv[1]))

