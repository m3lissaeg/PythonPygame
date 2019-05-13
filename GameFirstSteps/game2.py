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
        self.rect.x = p[0] #rect modifies the position
        self.rect.y = p[1]
        #velocidad:

        self.speedx =0
        self.speedy =0
    
    def update(self): #metodo heredado de la super clase sprite para actualizar los parametros
        self.rect.x += self.speedx
        self.rect.y += self.speedy

#c---------------

class Enemies(pygame.sprite.Sprite):
    
    """ Docstring clase cuadro """

    def __init__(self, p, color = SALMON): # p is the point where the object is going to be shown
        #super(Gamer, pygame.sprite.Sprite.__init__())
        pygame.sprite.Sprite.__init__(self)

        #image is the Sprite atribute 

        self.image = pygame.Surface([20, 20])
        self.image.fill(SALMON)
        self.rect = self.image.get_rect() # this returns 4 args: pos y, pos y , width , height 
        self.image.fill(color)
        self.rect.x = p[0] #rect modifies the position
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
    gamer = Gamer([300, 400])
    gamer.speedx = 5

    #adiciono el gamer al grupo para monitorear lo que sucede con los gamersGroup

    gamersGroup.add(gamer)

    #creacion y adicion al grupo de los Enemies

    enemiesGroup = pygame.sprite.Group()

    for i in range (10):
        r = Enemies([20, 20])
        r.rect.x  = random.randrange(WIDTH - r.rect.width)
        r.rect.y = random.randrange(500)
        r.speedx= random.randrange(10)
        enemiesGroup.add(r)

    screen.blit(gamer.image, [100, 100])

    
    end = True
    reloj = pygame.time.Clock()
    

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gamer.speedx= 5
                gamer.speedy = 0
            
            if event.key == pygame.K_LEFT:
                gamer.speedx = -5
                gamer.speedy = 0

            if event.key == pygame.K_UP:
                gamer.speedy = -5
                gamer.speedx = 0

            if event.key == pygame.K_DOWN:
                gamer.speedy = 5
                gamer.speedx = 0

            
        #important position stuff:
        print( gamer.rect.left, gamer.rect.right, gamer.rect.top, gamer.rect.bottom)
        #important size stuff
        print( gamer.rect.width, gamer.rect.height)

        # Limits
        #right, left edges

        if gamer.rect.x > (WIDTH -gamer.rect.width):
            gamer.rect.x = WIDTH -gamer.rect.width
            gamer.speedx = 0
        
        if gamer.rect.x < 0:
            gamer.rect.x = 0
            gamer.speedx = 0
        
        #Up, down edges 

        if gamer.rect.y > (HEIGH -gamer.rect.height):
            gamer.rect.y = HEIGH -gamer.rect.height
            gamer.speedy = 0

        if gamer.rect.y < 0:
            gamer.rect.y = 0
            gamer.speedy = 0

# ----- control de limites para los rivales ---

        for e in enemiesGroup:
            if e.rect.x > (WIDTH -e.rect.width):
                e.rect.x = WIDTH -e.rect.width
                e.speedx = e.speedx *-1
                
            if e.rect.x < 0:
                e.rect.x = WIDTH -e.rect.width
                e.speedx = e.speedx *-1

        

        # control:
        gamersGroup.update()
        enemiesGroup.update()

        #referesh screen 

        screen.fill(BLACK)   
        enemiesGroup.draw (screen) 
        gamersGroup.draw (screen)    
        pygame.display.flip()
        reloj.tick(30)