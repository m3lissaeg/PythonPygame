import pygame
from math import radians, sin, cos, floor

import pygame
from math import radians, sin, cos, floor

BLACK = (0,0,0)


def drawAxis(c):
    pygame.draw.line(screen, color2, [c[0]/2, 0], [c[0]/2, c[1]] , 2)
    pygame.draw.line(screen, color2, [0, c[1]/2], [c[0], c[1]/2] , 2)


def transLine(p, c):
    """ This function receives the line "p" (array) and the weidht and height of the screen "c" (array too),
       then, it returns the line transformed"""

    return [int(c[0]/2 +p[0]), int (c[1]/2 -p[1])]

    # -----Cardioide fuctions ---
  
def Cardioide(amp, angle) :
    """ amp es la amplitud """
    # we know that: x= r cos o  ,  y = r sen o ,   r = a  ( 1+ cos o)
    # so...  x = a ( 1+ cos o) * cos  o       ,     y = a ( 1+ cos o) * sen  o 
    # The process will be:   polars -> cartes -> transform to draw in axis

    return [ amp* ( 1 + sin(angle))* cos(angle) , amp* ( 1 + sin(angle))* sin(angle) ]



def rotate(p, angle):
    """ This function rotates a point in clock wise way (used with right key)
    p is the point to rotate, and angle is the angle of rotationg in degrees """
    
    radAngle = radians(angle)
    return [floor(p[0] * cos(radAngle)+ p[1] * sin(radAngle)), floor(p[0] * sin(radAngle) - p[1] * cos(radAngle))]

   

if __name__ == '__main__':
    pygame.init()


    screenWH =[900, 600]
    screen = pygame.display.set_mode(screenWH)
    pygame.display.flip()
    end = True
    color =  (50, 100, 250)
    color2 = (0, 200, 250)
    pos =()
    origin=[450, 300]
    point1 = [20, 30]
   # cardList= []
    rotAngle = 3

    
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False
                
            drawAxis(screenWH)
            

            if event.type == pygame.KEYDOWN:
    
                if event.key == pygame.K_LEFT: 
                    rotAngle -= 3
                    cardList= []


                if event.key == pygame.K_RIGHT:      
                    rotAngle += 3  
                    cardList= []                                  

                for ang in range (0, 361):
            
                    # the cardioide point in pygame screen
                    cardi = Cardioide(70, ang+rotAngle) 
                    #Rotate the point 
                    rotPoint = rotate(cardi, rotAngle)
                    #Transform the point to my screen axis
                    transline = transLine(rotPoint, screenWH)
                    #append the transformed point to the list:
                    cardList.append(transline)
                       
                                         
                    
                #Draw the list of transformed points in screen   
                screen.fill(BLACK)    
                pygame.draw.polygon(screen, color2, cardList )
                pygame.display.flip()
            