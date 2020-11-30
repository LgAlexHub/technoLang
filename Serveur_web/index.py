#!/usr/bin/python3
import cgi 
import cgitb
import function.pageMaker as pageMaker
import function.unicaen_search_engine as engine
cgitb.enable()
import json 


file = open("./ressources/res.json","r")
jsonContent = json.load(file)
form = cgi.FieldStorage()

print("Content-type: text/html; charset=utf-8\n")
if (form.getvalue("search")!=None):
    moteur = engine.unicaenSearchEngine("./ressources/res.json")
    res = moteur.matchEntireReq(form.getvalue("search"))
    page = pageMaker.makeResPage(res,jsonContent)
else:
    page = pageMaker.makeHomePage()
print(page)