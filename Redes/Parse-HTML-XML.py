from bs4 import BeautifulSoup
import urllib
xml = open("teste.xml", "r").read()

#####Parse documentos html ##########
###contents = urllib.urlopen('http://thehackerway.com').read()
##bs = BeautifulSoup(contents, 'lxml')
##print ("Titulo : " + str(bs.title))
##print (bs.meta)
##print (bs.meta['content'])
#print (bs.meta.parent)

##metas = bs.find_all('metas')
##for meta in metas:
##    print meta

##links = bs.find_all('links')
##for link in links:
##    print link

####headers = bs.find_all("div", id ="header")
####for header in headers:
####    captions = header.find_all("div", id ="caption")
#####    for caption in captions
####        print (caption)

###forms = bs.find_all('form')
###for form in forms:
###    print form

####parse de Documentos XML#########
bs = BeautifulSoup(xml, 'lxml')
###print (bs)
print (bs.note.to.text)
print (bs.note.to)
notes = bs.find_all("note")
for note in notes:
    print note