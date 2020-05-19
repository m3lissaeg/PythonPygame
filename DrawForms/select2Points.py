import pygame
from math import radians, sin, cos, floor
BLACK = (0,0,0)

def drawAxis(c):
    pygame.draw.line(screen, color, [c[0]/2, 0], [c[0]/2, c[1]] , 2)
    pygame.draw.line(screen, color, [0, c[1]/2], [c[0], c[1]/2] , 2)


def transLine(p, c):
    """ This function receives the line "p" (array, point coord) and the weidht and height 
    of the screen "c" (array too), then, it returns the point transformed"""
    return ([c[0]/2 +p[0], c[1]/2 -p[1]])


def rotateCounterCl(p, angle):
    """ p is the point to rotate, and angle is the angle of rotationg in degrees """
    
    radAngle = radians(angle)
    return [floor(p[0] * cos(radAngle)-p[1] * sin(radAngle)), floor(p[0] * sin(radAngle) + p[1] * cos(radAngle))]



if __name__ == '__main__':
    pygame.init()

    screenWH =[900, 600]
    center =[450, 300]
    point3 =  [100, 200]
    point4= [50, 250]
    screen = pygame.display.set_mode(screenWH)
    pygame.display.flip()
    end = True
    color =  (250, 0, 250)
    posList = []
    n = 3

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                e = list(event.pos)
                
                if (e[0] < center[0] and e[1]> center[1]):
                    posList.append(event.pos)          
                    
            #Dibujar la linea rotando 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:    
                    n +=3 

                if event.key == pygame.K_LEFT:      
                    n -=3            

                #dibuja la linea con la rotacion
                point1 = posList[0]
                point2 = posList[1]

                print(posList)

                pointRotated1 = rotateCounterCl(point1, n)
                pointRotated2 = rotateCounterCl(point2, n)
                pygame.draw.line(screen, color, pointRotated1, pointRotated2 , 2)
                pygame.display.flip()
                screen.fill(BLACK)  
                
                

                
                                 