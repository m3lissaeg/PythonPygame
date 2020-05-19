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


def calcularDistancia(point, x): #recibe la coordenada del punto y el centro en x, ya que la reflexion 
    #sera tomando como referencia el eje y
    return [(x + (x-point[0])) , point[1]]




if __name__ == '__main__':
    pygame.init()

    screenWH =[900, 600]
    center =[450, 300]
    point3 =  [100, 200]
    point4= [50, 250]
    point1 = []
    point2 = []
    screen = pygame.display.set_mode(screenWH)
    pygame.display.flip()
    end = True
    color =  (250, 0, 250)
    posList = []
    n = 3
    flag = 1


    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False


            drawAxis(screenWH)

            if ((event.type == pygame.MOUSEBUTTONUP) and (flag ==1)):
                flag = 2
                point1 = pygame.mouse.get_pos()

            if ((event.type == pygame.MOUSEBUTTONDOWN) and (flag ==2)):
                print("paso por aqui")
                flag = 4
                point2 = pygame.mouse.get_pos()


                pygame.draw.polygon(screen,color,[point1,point2,center],1)

                point1R = calcularDistancia(point1, center[0])
                point2R = calcularDistancia(point2, center[0])                 
                    
                pygame.draw.polygon(screen,color,[point1R,point2R,center],1)

            pygame.display.flip()
                