import pygame

#TODO: lista de listas
BLACK = (0,0,0)
ANCHO = 1024
ALTO = 384
ANCHOCORTE= 32
ALTOCORTE = 32
#FILA = 0
#COLUMNA = 1
listaSprites =[]
listaFila =[]

end = True


def FillMatrix(img, anchoCorte, altoCorte):
    cont = 0
    cont2 =0

    for FILA in range(12):

        #Agregar todas la columnas de la primera fila de sprites
        for COLUMNA in range (32):
            cuadro2 = img.subsurface(COLUMNA * 32, FILA * 32, anchoCorte, altoCorte) #Usando la formula 
            listaFila.append(cuadro2)
            cont +=1 #suma 12 veces hasta 32, es decir 384

        listaSprites.append(listaFila)
        cont2 +=1
    
    return listaSprites


if __name__ == '__main__':
    pygame.init()

    pantalla = pygame.display.set_mode([ANCHO ,ALTO])
    img = pygame.image.load('/home/melii/Documents/Python/game/terrenogen.png')

    cuadro = img.subsurface(0, 0, 100, 150) #Posicion 0, 0 recorta 100 de ancho y 150 de largo

    j = FillMatrix(img, ANCHOCORTE, ALTOCORTE)
    print(j)

    pantalla.blit(cuadro, [0,0])
   # pantalla.blit(img, [0,0])
    pygame.display.flip()

    info = img.get_rect() #obtener el ancho y el alto de la imagen
    anchoIm = info[2]
    altoIm = info[3]
    clock = pygame.time.Clock()


    #...........

    concol=0
    pantalla.blit(j[0][concol], [10,10] )
    pygame.display.flip()
    concol +=1

    if concol  == 2:
        concol =0
    clock.tick(10)


    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

            
                
                

                
                                 