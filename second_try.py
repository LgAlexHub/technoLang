import json
import re 
import glob 
import time
files = open("models.json","r")
content = json.load(files)
files.close()
dicoTest={}

for path in glob.glob("corpus_multi/*/test/*"):
    _,lang,corpus,filename = re.split("/",path)
    fichier = open(path,"r")
    chaine = fichier.read()
    mots = chaine.split()
    if lang not in dicoTest:
        dicoTest[lang]={}
    for mot in mots : 
        if mot not in dicoTest[lang]:
            dicoTest[lang][mot] = 1
        else : 
            dicoTest[lang][mot] =dicoTest[lang][mot] +1 

res={}
for lng in dicoTest: 
    L = sorted([[eff,mot]for mot,eff in dicoTest[lng].items()],reverse=True)
    res[lng] = L

final={}
#faire un set 
for lng in res:
    final[lng]={}
    for i in range(10):
        final[lng][i] = res[lng][i]


p = open ("test.json","w")
p.write(json.dumps(final,indent=2,ensure_ascii=False))
p.close()