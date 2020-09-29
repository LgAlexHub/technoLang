
import nltk
from nltk.book import *

def __richesseLexicale(text):
    nbMots = len(text)
    text.tokens = [t.lower() for t in text.tokens]
    richesse = len(text.vocab())/nbMots
    return richesse

for text in gutenberg.fileids():
   print(text+" : "+str(__richesseLexicale(Text(gutenberg.words(text)))))