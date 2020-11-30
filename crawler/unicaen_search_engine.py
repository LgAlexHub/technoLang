import pandas 
import numpy as np
import json
import pprint
from sklearn.feature_extraction.text import TfidfVectorizer

class unicaenSearchEngine():
    ###
    #    Une classe créant des matrices TFIDF afin de retourner le lien le plus utile en fonction du terme rechercher
        
    #    ...

    #    Attributes
    #    ...
    #    json : DataFrame
    #    corpus : DataFrame
    #    vectorizer : TfidfVecorizer
    #    X : sparse matrix
    ###

    def __init__(self,path, printOut = False):
    ###
    #Parameters
    #....
    #path : str
    #    Chemin du json à lire
    #printOUt : bool, optional
    #    Affiche divers informations sur la matric créer si = True
    ###
        self.json = pandas.read_json(path)
        self.corpus = self.json["text"]
        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.corpus) 
        if (printOut != False):
            self.showDimension()
            self.showXToArray()
            self.showDataGramme()
            self.showFeature()

    def showDataGramme(self):
    ###
    # Affiche les urls du json
    ###
        print("DATAGRAM : ",self.json['url'])
        
    def showFeature(self):
    ###
    # Affiche une map des termes avec leurs indices
    ###
        print("FEATURES : ",self.vectorizer.get_feature_names())
        
    def showDimension(self):
    ###
    # Affiche les dimensions de notre matrice TfIdf
    ###
        print("DIMENSION",self.X.shape)

    def filter_crawled_data__by_url(self,url):
    ###
    #  Indique si l'url passé en paramètre est dans notre datagramme 
    #  Parameters
    #  ...
    #  url : str 
    #   L'url a tester
    #  ...
    #  Retun 
    #  bool   
    #   un booléen indiquant la présence de l'url
    ###
        return self.json[self.json["url"]==url]
    
    def showXToArray(self):
    ###
    #   Affiche la matrice TfIdf sous forme de tableau   
    ###
        print("X TO ARRAY : \n",self.X.toarray())

    def minimal_test(self,url):
    ###
    # Teste l'existence du lien est affiche des informations sur ce lien
    ###
        res = self.filter_crawled_data__by_url(url)
        if not (res.empty) :
            print("Url à cette indice",self.json["url"][res.index])
            print("Lien à cette indice = ", self.json["lien"][res.index])
            print("(Numéro du document, numéro du termes dans la matrice)",self.X[:,res.index].toarray())
            print("Terme avec le plus gros coeff",max(self.X[:,res.index]))
    
    def search(self,terme):
    ###
    #   Cherche un terme dans notre dataFrame et renvoie le document avec le plus gros coefficient tfidf
    #   
    #   Parameters 
    #   ...
    #   terme : str
    #       Terme a rechercher dans notre matrice
    #   Return 
    #   ...
    #       list de lien avec leur coefficient classé dans l'ordre croissant
    ###
        descriptor_col = self.vectorizer.vocabulary_.get(terme)
        if(descriptor_col == None):
            return None
        subMatrix = self.X[:,descriptor_col]
        weigth_in_sub_matrix=np.sort(subMatrix.data)[::-1]
        indice_in_sub_matrix=np.argsort(subMatrix.data)[::-1]
        docs_ld = subMatrix.tocoo().row[indice_in_sub_matrix]
        urls = [self.json["url"][id] for id in docs_ld]
        return list(zip(urls,weigth_in_sub_matrix))

    def matchEntireReq (self,phrase):
        dictionnary = {}
        words = phrase.split(' ')
        for word in words : 
            res = self.search(word)
            if not(res == None):
                for element in res : 
                    if not(element[0] in dictionnary):
                        dictionnary[element[0]]= [0,[]]
                    dictionnary[element[0]][0]+= element[1]
                    if not(word in dictionnary[element[0]][1]):
                        dictionnary[element[0]][1].append(word)
                sort = sorted(dictionnary.items(), key = lambda  colonnes : colonnes[1],reverse=True)
                with open('res_search.json',"w") as ouput:
                    ouput.write(json.dumps(sort,indent=4,ensure_ascii=False))
            else : 
                print (word,"None")
                
                
                
                
                
            
                    

newDF = unicaenSearchEngine("./unicaen_crawler/res.json")
newDF.matchEntireReq("contact")
