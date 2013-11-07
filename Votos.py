import os
import re

# Compilo las RegExp que voy a usar
REcabecera=re.compile("<tr >(.*?)</tr>", re.DOTALL)
REcolumnas=re.compile("<th .*?>(.*?)</th>")
REdataPartido=re.compile('<tr>\s*(<th class="alaizquierda".*?)</tr>', re.DOTALL)
REnombrepartido = re.compile('<th .*?>(.*?)</th>')
REvotosPartido = re.compile('<td .*?>(.*?)</td>')
REinvalidos = re.compile('<tr>\s+(<th class="c.*?)</tr>',re.DOTALL)


salida= open("VotosDiputados.csv", "w")
idVoto=1
partidos=open("Partidos.csv").readlines()
indicePartidos={}
for partido in partidos:
    dataPartido=partido.strip().split(",")
    indicePartidos[dataPartido[1]+"-"+dataPartido[2]]=dataPartido[0]

archivosMesa= open("listadoMesas.txt").readlines()
os.chdir("/home/nico/PartidoPirata/elecciones/www.resultados.gob.ar/telegramas")

for archivoMesa in archivosMesa:
    lugar = archivoMesa.strip().split("/")
    distrito=lugar[0]
    municipio= lugar[1]
    circuito=lugar[2]
    mesa=lugar[3][-9:-5]
    f= open (archivoMesa.strip(),  encoding="latin-1")
    data = f.read()
    f.close()
    try:
        cabecera = REcabecera.findall(data)
        if cabecera==[]:
            print ("error en ",archivoMesa )
            continue
        else: 
            cabecera=cabecera[0]
        columnas= REcolumnas.findall(cabecera)
        for i in range(len(columnas)):
            if columnas[i] == "Diputados Nacionales":
                columnaDiputados=i
        
        dataPartido = REdataPartido.findall(data)
        dataPartido += REinvalidos.findall(data)[1:]
        for partido in dataPartido:
            nombrepartido=REnombrepartido.findall(partido)[0]
            votosPartido=REvotosPartido.findall(partido)[columnaDiputados-1]
            if(votosPartido=="&nbsp;"):
                votosPartido=0
            else:
                votosPartido=int(votosPartido)
            
            try:
                idPartido=indicePartidos[distrito+"-"+nombrepartido.strip()]
                print(str(idVoto)+","+distrito+mesa+","+ idPartido+","+ str(votosPartido), file=salida)
                idVoto+=1
            except KeyError:
                #Partido de eleccion municipal
                pass
    except:
        print(archivoMesa)
        raise
