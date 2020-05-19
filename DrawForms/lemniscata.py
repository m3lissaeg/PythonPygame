
import pygame
from math import radians, sin, cos, floor, sqrt

BLACK = (0,0,0)


def drawAxis(c):
    pygame.draw.line(screen, color, [c[0]/2, 0], [c[0]/2, c[1]] , 2)
    pygame.draw.line(screen, color, [0, c[1]/2], [c[0], c[1]/2] , 2)


def transLine(p, c):
    """ This function receives the line "p" (array) and the weidht and height of the screen "c" (array too),
       then, it returns the line transformed"""

    return [int(c[0]/2 +p[0]), int (c[1]/2 -p[1])]

    

  
def lemniscata(amp, angle) :
    """ amp es la amplitud """
    # we know that: x= r cos o  ,  y = r sen o ,   r = a  ( 1+ cos o)
    # The process will be:   polars -> cartes -> transform to draw in axis
    x =  ( amp* cos(2 *angle)) * cos(angle)
    y =  ( amp* cos(2 *angle)) * sin(angle)

    return [ x, y]


   

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
    amp = 70
    

    
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False
                
            drawAxis(screenWH)

            if event.type == pygame.KEYDOWN:                                   
                
                
                if event.key == pygame.K_DOWN:  
                    amp -= 3    
                    
                        
                        
                if event.key == pygame.K_UP: 
                    amp += 3  

                for ang in range (0, 361):
                    cardi = lemniscata(amp, ang) # this returns the new coord where i should draw the line                                                                    
                    transline = transLine(cardi, screenWH)
                    #lisLemnisc.appemnd()
                    pygame.draw.line(screen, color, origin,  transline , 2)

                pygame.display.flip()
                screen.fill(BLACK)                    
                    

                
            