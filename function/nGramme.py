# coding: utf-8
import glob
import re 
import json

def fournisseurDeModel(N):
    mapPerCountry={}
    for path in glob.glob("corpus_multi/*/appr/*"):
        _,lang,corpus,filename = re.split("/",path)
        files = open(path)
        chaine = files.read().decode("utf-8")
        tableau_mot = []
        for x in range(len(chaine)-N):
            tableau_mot.append(chaine[x:x+N])
        if (lang not in mapPerCountry):
            mapPerCountry[lang]={}
        for word in tableau_mot:
            if word in  mapPerCountry[lang]:
                mapPerCountry[lang][word.lower()] = mapPerCountry[lang][word.lower()] +1
            else : 
                mapPerCountry[lang][word.lower()] = 1
    res={}
    for lng in mapPerCountry: 
        L = sorted([[eff,mot]for mot,eff in mapPerCountry[lng].items()],reverse=True)[:100]
        res[lng] = L
    files.close()
    p = open ("ModelsGrams/modelsN"+str(N)+".json","w")
    p.write(json.dumps(res,indent=2,ensure_ascii=False))
    p.close()

for x in range(10):
    fournisseurDeModel(x)