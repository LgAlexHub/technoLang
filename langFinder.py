import glob 
import re 
import json 

def text_finder(path):
    file = open(path)
    return file.read


def diagnostic_langue(text):
    dictionnary = {}
    chaine_split = text.split()
    for word in chaine_split:
        if word.lower() in dictionnary:
            dictionnary[word.lower()] = dictionnary[word.lower()] + 1
        else :
            dictionnary[word.lower()] = 1

