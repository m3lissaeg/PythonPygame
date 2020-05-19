import pygame
import random


#create groups to manupulate the objects that belong to the same class
#create groups to manupulate enemies, bullets,... don't manipulate one by one all the objects
# groups concept --> watch it on  line 32

#create class -> create group -> add objects to the group - upload object -> draw the groups

HEIGH = 600
WIDTH = 900
SALMON = (250, 128, 114)
WHITE = (255, 255, 255)
BLACK = [0,0,0]

class Gamer(pygame.sprite.Sprite):

    """ Docstring clase cuadro """

    def __init__(self, p, color = WHITE): # p is the point where the object is going to be shown
        #super(Gamer, pygame.sprite.Sprite.__init__())
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
        #super(Gamer, pygame.sprite.Sprite.__init__())
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

    gamersGroup = pygame.sprite.Group()
    gamer1 = Gamer([300, 400])
    gamer1.speedx = 5

    #adiciono el gamer1 al grupo para monitorear lo que sucede con los gamersGroup

    gamersGroup.add(gamer1)

    #creacion y adicion al grupo de los rivales

    rivales = pygame.sprite.Group()

    for i in range (10):
        r = Rival([20, 20])
        r.rect.x  = random.randrange(WIDTH - r.rect.width)
        r.rect.y = random.randrange(500)
        r.speedx= random.randrange(10)
        rivales.add(r)

    screen.blit(gamer1.image, [100, 100])

    
    end = True
    reloj = pygame.time.Clock()
    

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gamer1.speedx= 5
                gamer1.speedy = 0
            
            if event.key == pygame.K_LEFT:
                gamer1.speedx = -5
                gamer1.speedy = 0

            if event.key == pygame.K_UP:
                gamer1.speedy = -5
                gamer1.speedx = 0

            if event.key == pygame.K_DOWN:
                gamer1.speedy = 5
                gamer1.speedx = 0

            
        #important position stuff:
        print( gamer1.rect.left, gamer1.rect.right, gamer1.rect.top, gamer1.rect.bottom)
        #important size stuff
        print( gamer1.rect.width, gamer1.rect.height)

        # Limits
        #right, left edges for gamer

        if gamer1.rect.x > (WIDTH -gamer1.rect.width):
            gamer1.rect.x = WIDTH -gamer1.rect.width
            gamer1.speedx = 0
        
        if gamer1.rect.x < 0:
            gamer1.rect.x = 0
            gamer1.speedx = 0
        
        #Up, down edges for enemies

        if gamer1.rect.y > (HEIGH -gamer1.rect.height):
            gamer1.rect.y = HEIGH -gamer1.rect.height
            gamer1.speedy = 0

        if gamer1.rect.y < 0:
            gamer1.rect.y = 0
            gamer1.speedy = 0

# ----- control de limites para los rivales ---

        for riv in rivales:
            if riv.rect.x > (WIDTH -riv.rect.width):
                riv.rect.x = WIDTH -riv.rect.width
                riv.speedx = riv.speedx *-1
                
            if riv.rect.x < 0:
                riv.rect.x = WIDTH -riv.rect.width
                riv.speedx = riv.speedx *-1

        ls = pygame.sprite.spritecollide(gamersGroup, rivales, False)
        for b in ls:
            if (
                .rect.right > b.rect.left) and (
                .velxx >0):
                
                .rect.right = b.rect.left
                
                .velx= 0
                
                .sonido.play()        

        # control:
        gamersGroup.update()
        rivales.update()

        #referesh screen 

        screen.fill(BLACK)   
        rivales.draw (screen) 
        gamersGroup.draw (screen)    
        pygame.display.flip()
        reloj.tick(30)