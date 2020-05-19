import pygame
from math import radians, sin, cos, floor
import random

BLACK= (0,0,0)


def drawAxis(c):
    pygame.draw.line(screen, color, [c[0]/2, 0], [c[0]/2, c[1]] , 2)
    pygame.draw.line(screen, color, [0, c[1]/2], [c[0], c[1]/2] , 2)


def transLine(p, c):
    """ This function receives the line "p" (array, point coord) and the weidht and height of the screen "c" (array too),
        then, it returns the point transformed"""
    print(str(c[0]/2 ) + "+"  + str(p[0]))
    print(str(c[1]/2 ) + "-"  + str(p[1]))
    print (" ------ ")

    return ([c[0]/2 +p[0], c[1]/2 -p[1]])


def rotateCounterCl(p, angle):
    """ p is the point to rotate, and angle is the angle of rotationg in degrees """
    
    radAngle = radians(angle)
    return [floor(p[0] * cos(radAngle)-p[1] * sin(radAngle)), floor(p[0] * sin(radAngle) + p[1] * cos(radAngle))]



if __name__ == '__main__':
    pygame.init()

    screenWH =[1000, 1500]
    screen = pygame.display.set_mode(screenWH)
    pygame.display.flip()
    end = True
    color =  (250, 0, 250)
    color2 =  (250, 200, 50)
    
    point1 = [-40, 10]
    point2 = [30, 10]
    point3 = [0, 50]
    listaPuntos=[  transLine(point1, screenWH) ,  transLine(point2, screenWH) ,  transLine(point3, screenWH)  ]
    i = 3 # cantidad de puntos que tiene la lista
    print(listaPuntos)
    

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

            drawAxis(screenWH) #dibujar el eje de referencia
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:
                    listaPuntos = []
                    i += 1
                    for e in range(i):
                        randX = random.randrange(-80, 80, 1)
                        randY = random.randrange(-80, 80, 1)
                        randPoint = transLine( [randX, randY], screenWH)
                        listaPuntos.append(randPoint)

                
                if event.key == pygame.K_d:
                    i = len(listaPuntos)
                    if i>3:
                        listaPuntos.pop()
                    else:
                        listaPuntos=[  transLine(point1, screenWH) ,  transLine(point2, screenWH) ,  transLine(point3, screenWH)  ]

        

                        
                screen.fill(BLACK)
                pygame.draw.polygon(screen, color, listaPuntos)
                print(listaPuntos)
                pygame.display.flip()
            