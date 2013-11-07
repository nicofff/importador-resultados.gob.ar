import os
import re
os.chdir("/home/nico/PartidoPirata/elecciones/www.resultados.gob.ar/telegramas")

for i in range(1, 25):
    distrito= str(i).rjust(2, "0");
    f= open ("IMUN"+str(distrito)+".html", encoding="latin-1")
    municipios = re.findall("([0-9]{3}) - ([^<]*)", f.read())
    for municipio in municipios:
        print (str(distrito)+municipio[0]+","+str(distrito)+","+municipio[1].strip()+","+municipio[0])
    f.close()
