import os
import re
os.chdir("/home/nico/PartidoPirata/elecciones/www.resultados.gob.ar/telegramas")
idPartido=1
for i in range(1, 25):
    distrito= str(i).rjust(2, "0");
    if distrito=="12":
        filename= str(distrito)+"/001/0001A/"+str(distrito)+"0010001A0001.html"
    elif distrito=="17":
        filename= str(distrito)+"/001/0001A/"+str(distrito)+"0010001A1001.html"
    elif distrito=="19":
        filename = "19/001/0002/190010002_0391.html"
    elif distrito=="21":
        filename = "21/001/0402/210010402_0001.html"
    else:
        filename= str(distrito)+"/001/0001/"+str(distrito)+"0010001_0001.html"
    f= open (filename,  encoding="latin-1")
    partidos = re.findall('<th class="alaizquierda">(.*?)</th>', f.read())
    f.close()
    for partido in partidos:
        print (str(idPartido)+","+ distrito+","+partido)
        idPartido+=1
