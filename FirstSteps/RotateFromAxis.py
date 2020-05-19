import pygame
from math import radians, sin, cos, floor

def rotateCounterCl(p, angle):
        """ p is the point to rotate, and angle is the angle of rotation"""
        radAngle = radians(angle)
        return [floor(p[0] * cos(radAngle)-p[1] * sin(radAngle)), floor(p[0] * sin(radAngle) + p[1] * cos(radAngle))]

  

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



    def drawAxis(c):
        pygame.draw.line(screen, color, [c[0]/2, 0], [c[0]/2, c[1]] , 2)
        pygame.draw.line(screen, color, [0, c[1]/2], [c[0], c[1]/2] , 2)


    def transLine(p, c):
        """ This function receives the line "p" (array) and the weidht and height of the screen "c" (array too),
            then, it returns the line transformed"""

        return ([c[0]/2 +p[0], c[1]/2 -p[1]])


    
    while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = False

                drawAxis(screenWH)
                transline = transLine(point1, screenWH)
                pygame.draw.line(screen, color, origin, transline , 2)
                
                point1Rotated = transLine(rotateCounterCl(point1 , 90), screenWH)
                print(point1Rotated)
                pygame.draw.line(screen, color, origin, point1Rotated, 2)
                pygame.display.flip()