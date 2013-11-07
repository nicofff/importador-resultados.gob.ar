import os
import re
os.chdir("/home/nico/PartidoPirata/elecciones/www.resultados.gob.ar/telegramas")
id=1

for i in range(1, 25):
    distrito= str(i).rjust(2, "0");
    f= open ("IMUN"+str(distrito)+".html", encoding="latin-1")
    municipios = re.findall("([0-9]{3}) - ([^<]*)", f.read())
    f.close()
    for municipio in municipios:
        codigoMunicipio=str(distrito)+municipio[0]
        g= open("ICIR"+codigoMunicipio+".html", encoding="latin-1")
        circuitos = re.findall("  >([0-9]{4}[A-Z]?)<", g.read())
        for circuito in circuitos:
            print (str(id)+","+codigoMunicipio+","+circuito)
            id+=1
        
    
