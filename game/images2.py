import pygame

#TODO: hacer funcion lista de listas 
#TODO: entender como funciona la clase jugador e implementarle el metodo de recortar
#TODO: hacerlo con el ave y que cuando vuele tenga mayor velocidad
#TODO: Implemtenar bloques con textura: colisiones
#En las proximas clases veremos mapeo: control de la pantalla, con fondo que se mueve y capa de colision


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
cont = 0
cont2 =0
clock = pygame.time.Clock()

# ---- Class Jugador ----------------------------------------------------

class Jugador (pygame.sprite.Sprite):

    def __init__(self, mat_i, pos_ini):
        pygame.sprite.Sprite.__init__(self)
        self.dir = 0
        self.concol =0
        self.m = mat_i
        self.image = self.m[self.dir][self.concol]
        self.rect = self.image.get_rect()
        self.rect.x = pos_ini[0]
        self.rect.y = pos_ini[1]
        self.velx=  0
        self.vely= 0


    def update(self):
        self.rect.y += self.vely
        self.rect.x += self.velx
        self.dir +=1
        if self.dir >2:
            self.dir=0

   
# --------------------- Fill Matrix function ----------------

def FillMatrix(img, anchoCorte, altoCorte):
    cont = 0
    cont2 =0

    for FILA in range(8):

        #Agregar todas la columnas de la primera fila de sprites
        for COLUMNA in range (12):
            cuadro2 = img.subsurface(COLUMNA * 32, FILA * 32, anchoCorte, altoCorte) #Usando la formula 
            listaFila.append(cuadro2)
            cont +=1 #suma 12 veces hasta 32, es decir 384

        listaSprites.append(listaFila)
        cont2 +=1
    
    return listaSprites

# width 384 --> 12 columnas, height 256 -->8 filas

# ----------------------------- Main -------------------------------------

if __name__ == '__main__':
    pygame.init()

    pantalla = pygame.display.set_mode([ANCHO ,ALTO])
    img = pygame.image.load('/home/melii/Documents/Python/game/animales.png')


    #fondo:
   # fondo = pygame.image.load('/home/melii/Documents/Python/game/fondo.png')
    fx = 0 #posicion incial del fonfo
    vx = 0 #velocidad conla que se va a desplazar la imagen
    #

    cuadro = img.subsurface(0, 0, 100, 150) #Posicion 0, 0 recorta 100 de ancho y 150 de largo


    m = FillMatrix(img, ANCHOCORTE, ALTOCORTE)


    j= Jugador(m, [100, 50])
    jugadores = pygame.sprite.Group()
    jugadores.add(j)




   # pantalla.blit(img, [0,0])

    info = img.get_rect() #obtener el ancho y el alto de la imagen
    anchoIm = info[2]
    altoIm = info[3]


    #...........

    pantalla.fill(BLACK)
    jugadores.update()

   
    jugadores.draw(pantalla)
    pygame.display.flip()
    clock.tick(10)
    
    fx += vx # desplazo la imagen de la pantalla
    limx = 550

   


    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                j.dir = 2
                j.velx = 5
                j.vely= 0
            if event.key == pygame.K_LEFT:
                j.dir = 1
                j.velx = -5
                j.vely= 0
            if event.key == pygame.K_DOWN:
                j.dir = 0
                j.velx = 0
                j.vely = 5

            if event.key == pygame.K_UP:
                j.dir = 0
                j.velx = 0
                j.vely = -5


            