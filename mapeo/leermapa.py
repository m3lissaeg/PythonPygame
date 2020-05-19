import pygame
import random
import math
import configparser




mapa = configparser.ConfigParser()
mapa.read('mapa.map')
cad_map = mapa.get('info', 'mapa')
ls_mapa=cad_map.split('\n')


ANCHO = 640
ALTO = 480
NEGRO = [0,0,0]
BLANCO = [255,255,255]
VERDE = [0,255,0]
ROJO = [255,0,0]


def imgcut32(img, alto, ancho, anch_pj, alt_pj):
    m=[]

    for h in range(0,alto):
        ls=[]
        for i in range(0,ancho):
            cuadro = img.subsurface(i*anch_pj,h*alt_pj,anch_pj,alt_pj)
            ls.append(cuadro)
        m.append(ls)

    return (m)

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    img= pygame.image.load('terrenogen.png')

    fila=ls_mapa[3]

    an_cor=32
    al_cor=32

    m=imgcut32(img, 12, 32, 32,32)

    coon=0
    con=0
    pos_fila=0
    an_corte=32
    for fila in ls_mapa:
        pos_fila=an_corte*coon
        for c in fila:
            pos_col=an_corte*con
            pantalla.blit(m[int(mapa.get(c,'uy'))][int(mapa.get(c,'ux'))], [pos_col,pos_fila])
            con+=1
        con=0
        coon+=1
    print(fila)
    pygame.display.flip()

    reloj = pygame.time.Clock()
    fin = False
    fin_juego=False
    while not (fin or fin_juego):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True


        pygame.display.flip()
