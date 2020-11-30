#!/usr/bin/python3

import json
###
#   Renvoie le code html d'un head 
#
#   Parameters
#   ...
#   titre : str
#       titre de la page html
#   
#   Return
#   ...
#   str
#       Code html d'un header
###
def makeHeader(title):
    return " <!DOCTYPE html><head> <title>"+ title+" </title> <link rel='stylesheet' href='../ressources/style.css'/> <link rel='icon' href='../../ressources/logo_uni.ico'/> </head> <body>"

###
#   Renvoie le code html d'une navbar 
#
#   
#   Return
#   ...
#   str
#       Code html d'une navbar
###
def makeNavBar():
    return " <div class='nav'> <ul> <li> Unicaen - Web Finder </li> </ul> </div> "

###
#   Renvoie le code html d'un head 
#
#   
#   Return
#   ...
#   str
#       Code html d'un footer
###
def makeFooter():
    return "</html>"

###
#   Renvoie le code html d'un body html pour la page d'accueil 
#
#   
#   Return
#   ...
#   str
#       Code html du body de la page d'accueil
###
def makeBodyHome():
    return " <h4>Unicaen - Web Finder</h4> <div class='containerSearch'> <form action='./index.py' method='POST'> <input type='text' name='search' /> <input type='submit' value='Rechercher'/> </form> </div> </body>"

###
#   Renvoie le code html de la page d'accueil
#
#   
#   Return
#   ...
#   str
#       Code html de la page d'accuel
###
def makeHomePage():
    return makeHeader("Web-Finder")+makeNavBar()+makeBodyHome()+makeFooter()

###
#   Renvoie le code html des réponses de la requêtes utilisateur
#
#   Parameters
#   ...
#   jsonP : array
#       les sites répondant le mieux à l'utilisateur
#   
#   bigJson : array
#       tout les sites stockés dans notre json
#   Return
#   ...
#   str
#       Code html des sites sous fomres de liste
###
def returnListOfSite(jsonP,bigJson):
    Str = "<ul>"
    if (jsonP == None):
        return "Aucun résultat..."
    else:
        for element in jsonP :
            for el in bigJson:
                if (el['url']==element[0]):
                    if (el['titre']==None):
                        Str+="<li><div class='displayRes'><a href='"+element[0]+"'/>Page sans titre</a><p><i>adresse: <a href='"+element[0]+"'>"+element[0]+"</a></i></p>"
                    else :
                        Str+="<li><div class='displayRes'><a href='"+element[0]+"'/>"+el['titre']+"</a>"
                    Str+="<p>Contient le(s) mot(s) suivant : </p>"
                    for word in element[1][1]:
                        Str+="<i>"+word+"</i> "
                Str+="</div></li>"               
        return Str+"</ul>"

###
#   Renvoie le code html de la page de résultat
#   Parameters
#   ...
#   jsonP : array
#       les sites répondant le mieux à l'utilisateur
#   
#   bigJson : array
#       tout les sites stockés dans notre json
#   Return
#   ...
#   str
#       Code html de la page des résultat
###
def makeResPage(jsonP,bigJson):
    return makeHeader("Web-Finder")+makeNavBar()+makeBodyHome()+returnListOfSite(jsonP,bigJson)+makeFooter()