import glob 
import json
import re 

mapPerCountry={}
for path in glob.glob("corpus_multi/*/appr/*"):
    _,lang,corpus,filename = re.split("/",path)
    files = open(path)
    chaine = files.read()
    mot=chaine.split()
    if (lang not in mapPerCountry):
        mapPerCountry[lang]={}
    for word in mot:
        if word in  mapPerCountry[lang]:
            mapPerCountry[lang][word.lower()] = mapPerCountry[lang][word.lower()] +1
        else : 
            mapPerCountry[lang][word.lower()] = 1;


res={}
for lng in mapPerCountry: 
    L = sorted([[eff,mot]for mot,eff in mapPerCountry[lng].items()],reverse=True)
    res[lng] = L
    
files.close()
p = open ("models.json","w")
p.write(json.dumps(res,indent=2,ensure_ascii=False))
p.close()