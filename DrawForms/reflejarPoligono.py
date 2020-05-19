import pygame
from math import radians, sin, cos, floor
BLACK = (0,0,0)
color2 = (240, 30, 20)

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


def calcularDistancia(point, x): #recibe la coordenada del punto y el centro en x, ya que la reflexion 
    #sera tomando como referencia el eje y
    return [(x + (x-point[0])) , point[1]]



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
        drawAxis(screenWH)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                e = list(event.pos)
                posList.append(event.pos) 
                         
                    
            #Dibujar el poligono
            if event.type == pygame.KEYDOWN:

                pygame.draw.polygon(screen, color2, posList )
                pygame.display.flip()

                polRefle = ReflePoligon ()
                
                
