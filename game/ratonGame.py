import pygame

ANCHO=640
ALTO=480
BLANCO=[255,255,255]
NEGRO=[0,0,0]
ROJO = [255, 0, 0]
VERDE = [0, 255, 0]

COLOR = [30, 40, 50]


#TODO: hacer que cuando se arrastre el cuadro movil hacia la linea, ella se desplace por la trayectoria de 
#la linea 

# algoritmo Montecarlo para juegos de azar 
#juegos plataforma 

class Cuadro(pygame.sprite.Sprite):
    def __init__(self, pos_ini,cl , name):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([50, 50])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=pos_ini[0]
        self.rect.y=pos_ini[1]


        self.name = name

        #velocidad del objeto en x  y en y
        self.velx = 0
        self.vely = 0


        self.click = False

    def update(self):
        if self.click==False:
            self.rect.x += self.velx
            self.rect.y += self.vely
        if self.click:
            self.rect.center= pygame.mouse.get_pos()



class CuadroStatic(pygame.sprite.Sprite):
    def __init__(self, pos_ini,cl, name ):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([100, 50])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=pos_ini[0]
        self.rect.y=pos_ini[1]

        self.name = name

        # Al darle click debe generar un objeto de tipo Cuadro normal, que se va a mover y se va a desplazar 
        # hacia la derecha si es rojo y hacia abajo si es verde        
        self.click = False

    def update(self):
        if self.click:
            self.rect.center= pygame.mouse.get_pos()


if __name__ == "__main__":
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    fin = False
    reloj = pygame.time.Clock()

    c1= CuadroStatic([50, 400], VERDE, "verde")
    c2= CuadroStatic([200, 400], ROJO, "rojo")     
    cuadros = pygame.sprite.Group()    
    #Agrego al grupoo los cuadros estaticos que estaran al final 
    #de la pantalla
    cuadros.add(c1)
    cuadros.add(c2)

    cuadrosMovil = pygame.sprite.Group()    #Grupo de los cuadros no estaticos, que se crean al dar click en alguno
    # de los cuadros de color 






    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if c1.rect.collidepoint(event.pos): #c1 es el cuadro verde
                    cNuevo = Cuadro(c1.rect, VERDE, "v")
                    cNuevo.click = True
                    cuadrosMovil.add(cNuevo)

                if c2.rect.collidepoint(event.pos):
                    cNuevo = Cuadro(c1.rect, ROJO, "r")
                    cNuevo.click = True
                    cuadrosMovil.add(cNuevo)

            if event.type == pygame.MOUSEBUTTONUP:
                cNuevo.click = False
                if cNuevo.name == "v":
                    cNuevo.vely = 5 # Velocidad hacia abajo
                
                if cNuevo.name == "r":
                    cNuevo.velx = 5

            

            
        pantalla.fill(NEGRO)
        cuadros.update()
        cuadrosMovil.update()
        cuadros.draw(pantalla)
        cuadrosMovil.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)

            
            