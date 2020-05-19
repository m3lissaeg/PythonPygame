import configparser

#TODO: dibujar el mapa en la pantalla usando la lista de puntos y simbolos para hacer eferencia a cada uno de los
#elemntos
#HAcer el recorte, ponerlo en un ciclo 
#Esta libreria tiene unos metodos queme permite leer cadenas

inteprete = configparser.configParser()
mapa = inteprete.read('mapa.map')
# print(mapa.sections())

#info general

print(mapa.items('info'))
print(mapa.get('info', 'origen'))
print(mapa.get('info', 'mapa'))
cadMapa =mapa.get('info', 'mapa')
lsMapa = cadMapa.split('\n')

con = 0
x =0
anCorte  =32
print(lsMapa)


fila = lsMapa[2] #imprimir columnas de la fila
for c in fila:
    y = anCorte * con
    print(c)
    print(mapa.get(c, 'ux'), mapa.get(c, 'uy'))
print(fila)

# for fila in lsMapa:
#     print(fila)



con = 0
for s in mapa.sections:
    print(s)
    print(mapa.items(s))
    print(mapa.get(s, 'ux'), mapa.get(s, 'uy') )
print(mapa.get('info', 'origen')