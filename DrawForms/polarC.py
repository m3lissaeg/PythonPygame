#Transformacion para dibujar una coordenada polar en el plano cartesiano
# Challenge : hacer que al presionar alguna tecla, cambie de posicion el cardioide


import pygame
from math import radians, sin, cos, floor

BLACK = (0,0,0)


def drawAxis(c):
    pygame.draw.line(screen, color, [c[0]/2, 0], [c[0]/2, c[1]] , 2)
    pygame.draw.line(screen, color, [0, c[1]/2], [c[0], c[1]/2] , 2)


def transLine(p, c):
    """ This function receives the line "p" (array) and the weidht and height of the screen "c" (array too),
       then, it returns the line transformed"""

    return [int(c[0]/2 +p[0]), int (c[1]/2 -p[1])]

    # -----Cardioide fuctions ---
  
def drawCardioideUp(amp, angle) :
    """ amp es la amplitud """
    # we know that: x= r cos o  ,  y = r sen o ,   r = a  ( 1+ cos o)
    # so...  x = a ( 1+ cos o) * cos  o       ,     y = a ( 1+ cos o) * sen  o 
    # The process will be:   polars -> cartes -> transform to draw in axis

    return [ amp* ( 1 + sin(angle))* cos(angle) , amp* ( 1 + sin(angle))* sin(angle) ]

def drawCardioideDown(amp, angle) :
    """ amp es la amplitud """
    # we know that: x= r cos o  ,  y = r sen o ,   r = a  ( 1+ cos o)
    # so...  x = a ( 1+ cos o) * cos  o       ,     y = a ( 1+ cos o) * sen  o 
    # The process will be:   polars -> cartes -> transform to draw in axis

    return [ amp* ( 1 - sin(angle))* cos(angle) , amp* ( 1 - sin(angle)) * sin(angle) ]


def drawCardioideL(amp, angle) :
    """ amp es la amplitud """
    # we know that: x= r cos o  ,  y = r sen o ,   r = a  ( 1+ cos o)
    # so...  x = a ( 1+ cos o) * cos  o       ,     y = a ( 1+ cos o) * sen  o 
    # The process will be:   polars -> cartes -> transform to draw in axis

    return [ amp* ( 1 - cos(angle))* cos(angle) , amp* ( 1 - cos(angle))* sin(angle) ]



def drawCardioideR(amp, angle) :
    """ amp es la amplitud """
    # we know that: x= r cos o  ,  y = r sen o ,   r = a  ( 1+ cos o)
    # so...  x = a ( 1+ cos o) * cos  o       ,     y = a ( 1+ cos o) * sen  o 
    # The process will be:   polars -> cartes -> transform to draw in axis

    return [ amp* ( 1 + cos(angle))* cos(angle) , amp* ( 1 + cos(angle))* sin(angle) ]



   

if __name__ == '__main__':
    pygame.init()


    screenWH =[900, 600]
    screen = pygame.display.set_mode(screenWH)
    pygame.display.flip()
    end = True
    color =  (250, 0, 250)
    pos =()
    origin=[450, 300]
    point1 = [20, 30]

    
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False
                
            drawAxis(screenWH)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: 
                    screen.fill(BLACK)           
                    for ang in range (0, 361):
                        cardi = drawCardioideR(70, ang) # this returns the new coord where i should 
                                                                    # draw the line
                        transline = transLine(cardi, screenWH)
                        # pygame.draw.circle(screen, color, transline , 2)
                        pygame.draw.line(screen, color, origin,  transline , 2)
                        pygame.display.flip()
                    
                if event.key == pygame.K_LEFT:   
                    screen.fill(BLACK)    
                    for ang in range (0, 361):
                        cardi = drawCardioideL(70, ang) # this returns the new coord where i should 
                                                                    # draw the line
                        transline = transLine(cardi, screenWH)
                        # pygame.draw.circle(screen, color, transline , 2)
                        pygame.draw.line(screen, color, origin,  transline , 2)
                        pygame.display.flip()
                
                if event.key == pygame.K_DOWN:  
                    screen.fill(BLACK)                    
                    for ang in range (0, 361):
                        cardi = drawCardioideDown(70, ang) # this returns the new coord where i should 
                                                                        # draw the line
                        transline = transLine(cardi, screenWH)
                        # pygame.draw.circle(screen, color, transline , 2)
                        
                        pygame.draw.line(screen, color, origin,  transline , 2)
                        pygame.display.flip()
                        
                if event.key == pygame.K_UP:   
                    screen.fill(BLACK)                    
                    for ang in range (0, 361):
                        cardi = drawCardioideUp(70, ang) # this returns the new coord where i should 
                                                                    # draw the line
                        transline = transLine(cardi, screenWH)
                        # pygame.draw.circle(screen, color, transline , 2)
                        
                        pygame.draw.line(screen, color, origin,  transline , 2)
                        pygame.display.flip()
                    

                
            