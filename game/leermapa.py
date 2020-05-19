import pygame

ANCHO=640
ALTO=480
BLANCO=[255,255,255]
NEGRO=[0,0,0]



#TODO: que al principi o el ken este moviendose adelante y atras, al oprimir una tecla que ejecute otra accion
#TODO: que lance un poder con abajo diagonal derecha

def cortarimg(img,fx,fy):
    # 'fx' es el numero de figuras que hay en el eje x
    # 'fy' es el numero de figuras que hay en el eje y
    #matriz que guarda la posicion de las imagenes ya recortadas
    m=[]
    #guarda la info de la imagen
    info=img.get_rect()
    ancho_img=info[2]   #guardo ancho de la imagen
    alto_img=info[3]    #guarda alto de la imagen

    for s in range(0,fx):
        ls=[]
        for i in range(0,fy):
            ls.append(img.subsurface(s*(ancho_img/fx),i*(alto_img/fy),(ancho_img/fx),(alto_img/fy)))
        m.append(ls)

    return m

class Jugador(pygame.sprite.Sprite):
    def __init__(self,mat_i, lim , pos_ini):
        pygame.sprite.Sprite.__init__(self)
        self.accion=3
        self.concol=0
        self.m=mat_i
        self.lim = lim# mariz de limites
        self.image = self.m[self.accion][self.concol]
        self.rect=self.image.get_rect()
        self.rect.x=pos_ini[0]
        self.rect.y=pos_ini[1]
        self.velx=0
        self.vely=0

    def update(self):
        self.image = self.m[self.accion][self.concol]

        if self.concol < self.lim[self.accion] :
            self.concol+=  1
        else:
            concol= 0




if __name__ == "__main__":
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    #IMagen con los terrenos a recortar
    img=pygame.image.load('/home/melii/Documents/Python/game/animales.png')

    #surface(posInicial,Zona a cortar)
    m = cortarimg(img,12,8)
    col=0
    accion = 0 #este cambia segn la fila que queira mostrar, cad afila muestra una accion distinta 

    jugadores = pygame.sprite.Group()
    lim = [3,3,2,4,1,3,4,4,6,0] #Arreglo con las filas, en donde se guarda la cantidad de sprites que hay por fila parra realizar una acción
    j = Jugador(m, lim, [100, 100])

    jugadores.add(j)

    fin=False
    reloj=pygame.time.Clock()


    for b in bloques: #bloque es el grupo de objetos 
        pos_ken=[j.rect.right, j.rect.y]
        if b.rect.collidepoint(pos_ken):
            print ("Me ha tocao")

            

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            
            #pantalla.fill(NEGRO)
            jugadores.draw(pantalla)

            
            
