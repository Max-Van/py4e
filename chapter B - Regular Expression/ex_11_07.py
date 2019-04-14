import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url=input('Enter URL: ')
#url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#url='http://py4e-data.dr-chuck.net/known_by_Nivedita.html'
urlt=url

#totalcount=7
#pos=18

totalc=input('Enter count:')
totalcount=int(totalc)

posi=input('Enter position:')
pos=int(posi)


html=urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

count = 0
linklist=list()
linklist.append(url)



for po in range(int(totalcount)) :
    html=urllib.request.urlopen(urlt).read()
    soup = BeautifulSoup(html,'html.parser')
    tags=soup('a')
    count = 0
    for tag in tags:
        count += 1
        if count == pos :
            urlitem=tag.get('href',None)
            linklist.append(urlitem)
            break
    urlt=urlitem
    urlitem= None

for it in linklist:
    print (it)
#print(linklist)
