import configparser

mapa = configparser.ConfigParser()
mapa.read('mapa.map')
#print(mapa.sections())
#info general
#print(mapa.items('info'))
#print(mapa.get('info', 'origen'))
#print(mapa.get('info', 'mapa'))

cad_map = mapa.get('info', 'mapa')
ls_mapa=cad_map.split('\n')
print (ls_mapa)

fila=ls_mapa[3]

con=0
x=0
pos_fila=0
an_corte=32

for c in fila:
    pos_col=an_corte*con
    print(c, pos_fila, pos_col)
    print(mapa.get(c,'ux'),mapa.get(c,'uy'))
    con+=1
print(fila)

'''
for fila in ls_mapa:
    print (fila)
'''

'''
#Seccion descripcion mapa
con=0
for s in mapa.sections():
    if con == 0:
        con+=1
    else:
        print(s)
        print(mapa.items(s))
        print(mapa.get(s,'ux'), mapa.get(s, 'uy'))
print (mapa.get('info', 'origen'))
'''
