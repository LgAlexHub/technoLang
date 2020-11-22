import nltk
import spacy
import json
import sys
from nltk.corpus import treebank
from pprint import pprint

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
def loadJsonFile(path):
    file = open (path)
    return json.load(file)

corpusArray = loadJsonFile('./ressources/corpus.json')   
## accès à un élément content_file['corpus'][indice]['text']


def init(text):
    tokens = nltk.word_tokenize(text)
    #print("===TOKEN===\n",tokens)
    pos_token = nltk.pos_tag(tokens)
    #print("===POSTAG===\n",pos_token)
    analyse = nltk.ne_chunk(pos_token)
    #pprint(analyse[0])
    #print(analyse[0].label())
    return analyse
    
def dictionnaryMakerNltk(text,jsonNameOuput="default"):
    tokens = nltk.word_tokenize(text)
    pos_token = nltk.pos_tag(tokens)
    analyse = nltk.ne_chunk(pos_token)
    dictionnary = {}
    for line in analyse:
        if (hasattr(line,"label")):
            if line.label() in dictionnary.keys():
                dictionnary[line.label()].append(line[0][0])
            else :
                dictionnary[line.label()] = [line[0][0]]
    if jsonNameOuput!="default" :
        res =[dictionnary,tokens]
        jsonWriter(jsonNameOuput,res,4,False)
    else:
        return dictionnary
       
        
def jsonWriter(names,data,indents=4,ascii = False):
    res = data
    with open("./ressources/"+names+".json","+w") as outfile:
            outfile.write(json.dumps(res,indent=indents,ensure_ascii=ascii))

def dictionnaryMakerSpacy(modelSpacyString, rawText ,jsonNameOuput = None):
    modele = spacy.load(modelSpacyString)
    document = modele(rawText)
    dictionnary = {}
    tokens =[]
    for entite in document.ents:
        if entite.label_ in dictionnary.keys():
            dictionnary[entite.label_].append(entite.text)
        else :
            dictionnary[entite.label_] = [entite.text]
    for token in document: 
        tokens.append(token.text)
    if jsonNameOuput!="default" :
        res =[dictionnary,tokens]
        jsonWriter(jsonNameOuput,res,4,False)
    else:
        return dictionnary


def _main():
    tabModelSpacy = ["fr_core_news_sm","fr_core_news_md","fr_core_news_lg","en_core_web_sm","en_core_web_md","en_core_web_lg"]
    if(sys.argv[1]=="nltk"):
        option = [sys.argv[1], int(sys.argv[2]), sys.argv[3]]
        dictionnaryMakerNltk(corpusArray['corpus'][option[1]]['text'],option[2])
        print("Vos option : type :",option[0]," / texte choisi :",option[1]," / nom json sortant : ",option[2])
    elif (sys.argv[1]=="all"):
        _genAll()
    else : 
        option = [sys.argv[1], int(sys.argv[2]), sys.argv[3],int(sys.argv[4])]
        dictionnaryMakerSpacy(tabModelSpacy[option[3]],corpusArray['corpus'][option[1]]['text'],option[2])
        print("Vos option : type :",option[0]," / texte choisi :",option[1]," / nom json sortant : ",option[2]," / type de modèle :",option[3])
    
def _genAll():
    print("Lancement de la génération de tout les json (attention cela peut durer longtemps)")
    tabModelSpacy = ["fr_core_news_sm","fr_core_news_md","fr_core_news_lg","en_core_web_sm","en_core_web_md","en_core_web_lg"]
    for x in range (10):
        print("//Génération nltk du texte ",x)
        dictionnaryMakerNltk(corpusArray['corpus'][x]['text'],"nltkJson"+str(x))
    for x in range (10):
        for y in range (6):
            print("//Génération spacy du texte ",x," modele numéro ",y)
            dictionnaryMakerSpacy(tabModelSpacy[y],corpusArray['corpus'][x]['text'],"spacy"+str(x))
_main()

