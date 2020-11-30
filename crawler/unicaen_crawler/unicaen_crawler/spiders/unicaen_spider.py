import scrapy
import json
from bs4 import BeautifulSoup,Comment

class QuotesSpider(scrapy.Spider):
    name = "unicaen"
    allowed_domains = ['unicaen.fr']
    
###
#   Déclenche le parse du robot sur le domaine demandé
###
    def start_requests(self):
        urls = [
            'http://www.unicaen.fr'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
###
#   Récupère le contenu du page web et créer un dictionnaire de données sur le domaine 
#	Forme dictionnaire {url: str, titre: str, contenu:str, liens[str]}
#
#   Parameters
#   ...
#   response : str
#       le code html récupérer par le robot
#   Return
#   ...
#   str
#       Code html des sites sous fomres d eliste
###
    def parse(self, response):
        page = response.url.split("/")[-2]
        body = response.css("body").get()
        bs = BeautifulSoup(body,'html.parser')
        text_in_element = [element.string for element in  bs.find_all(['a','p','h1','h2','h3','h4','h5','h6','div']) if element.string != None for s in element.stripped_strings]
        text =''.join(text_in_element)
        yield {'url' : response.url, 'titre' : response.css("head title::text").get(), 'lien' : response.css("a::attr(href)").getall(), 'text': text}
        for lien_brut in response.css("a::attr(href)").getall():
            if (self.allowed_domains[0] in lien_brut) and (response.meta['depth'] <= 1):
                lien = response.urljoin(lien_brut)
                yield scrapy.Request(lien,callback=self.parse)
        
        filename = './rawhtml/quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
