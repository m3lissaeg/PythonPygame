import pygame
import random


#crear grupos para maipular los objetos: por ejemplo: 
# grpos par los jugadores, para los enemigos, para las balas... , para no tener que manipular una  auna las variables
#concepto de grupos --> watch it on  line 32

#crear clase, grupo, objetos, adicionar los objetos al grupo y lulego se dibujan

HEIGH = 600
WIDTH = 900
SALMON = (250, 128, 114)
WHITE = (255, 255, 255)
BLACK = [0,0,0]

class Cuadro(pygame.sprite.Sprite):

    """ Docstring clase cuadro """

    def __init__(self, p, color = WHITE): # p is the point where the object is going to be shown
        #super(Cuadro, pygame.sprite.Sprite.__init__())
        pygame.sprite.Sprite.__init__(self)

        #image is the Sprite atribute 

        self.image = pygame.Surface([50, 50])
        self.image.fill(SALMON)
        self.rect = self.image.get_rect() # this returns 4 args: pos y, pos y , width , height 
        self.image.fill(color)
        self.rect.x = p[0] #rect encargado de mmodificar la posicion
        self.rect.y = p[1]
        #velocidad:

        self.speedx =0
        self.speedy =0
    
    def update(self): #metodo heredado de la super clase sprite para actualizar los parametros
        self.rect.x += self.speedx
        self.rect.y += self.speedy

#c---------------

class Rival(pygame.sprite.Sprite):
    
    """ Docstring clase cuadro """

    def __init__(self, p, color = SALMON): # p is the point where the object is going to be shown
        #super(Cuadro, pygame.sprite.Sprite.__init__())
        pygame.sprite.Sprite.__init__(self)

        #image is the Sprite atribute 

        self.image = pygame.Surface([20, 20])
        self.image.fill(SALMON)
        self.rect = self.image.get_rect() # this returns 4 args: pos y, pos y , width , height 
        self.image.fill(color)
        self.rect.x = p[0] #rect encargado de mmodificar la posicion
        self.rect.y = p[1]
        #velocidad:

        self.speedx =3
        self.speedy =0
    
    def update(self): #metodo heredado de la super clase sprite para actualizar los parametros
        self.rect.x += self.speedx
        self.rect.y += self.speedy



# ----------------------------------

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([900, 600]) # width   heigh

    jugadores = pygame.sprite.Group()
    jugador = Cuadro([300, 400])
    jugador.speedx = 5

    #adiciono el jugador al grupo para monitorear lo que sucede con los jugadores

    jugadores.add(jugador)

    #creacion y adicion al grupo de los rivales

    rivales = pygame.sprite.Group()

    for i in range (10):
        r = Rival([20, 20])
        r.rect.x  = random.randrange(WIDTH - r.rect.width)
        r.rect.y = random.randrange(500)
        r.speedx= random.randrange(10)
        rivales.add(r)

    screen.blit(jugador.image, [100, 100])

    
    end = True
    reloj = pygame.time.Clock()
    

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                jugador.speedx= 5
                jugador.speedy = 0
            
            if event.key == pygame.K_LEFT:
                jugador.speedx = -5
                jugador.speedy = 0

            if event.key == pygame.K_UP:
                jugador.speedy = -5
                jugador.speedx = 0

            if event.key == pygame.K_DOWN:
                jugador.speedy = 5
                jugador.speedx = 0

            
        #important position stuff:
        print( jugador.rect.left, jugador.rect.right, jugador.rect.top, jugador.rect.bottom)
        #important size stuff
        print( jugador.rect.width, jugador.rect.height)

        # Limits
        #right, left edges

        if jugador.rect.x > (WIDTH -jugador.rect.width):
            jugador.rect.x = WIDTH -jugador.rect.width
            jugador.speedx = 0
        
        if jugador.rect.x < 0:
            jugador.rect.x = 0
            jugador.speedx = 0
        
        #Up, down edges 

        if jugador.rect.y > (HEIGH -jugador.rect.height):
            jugador.rect.y = HEIGH -jugador.rect.height
            jugador.speedy = 0

        if jugador.rect.y < 0:
            jugador.rect.y = 0
            jugador.speedy = 0

# ----- control de limites para los rivales ---

        for riv in rivales:
            if riv.rect.x > (WIDTH -riv.rect.width):
                riv.rect.x = WIDTH -riv.rect.width
                riv.speedx = riv.speedx *-1
                
            if riv.rect.x < 0:
                riv.rect.x = WIDTH -riv.rect.width
                riv.speedx = riv.speedx *-1

        

        # control:
        jugadores.update()
        rivales.update()

        #referesh screen 

        screen.fill(BLACK)   
        rivales.draw (screen) 
        jugadores.draw (screen)    
        pygame.display.flip()
        reloj.tick(30)