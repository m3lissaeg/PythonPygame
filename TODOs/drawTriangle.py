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
    color2 =  (250, 100, 50)
    pos =()
    origin=[450, 300]
    pointlist = [[250,150], [680,150], [680, 400]]

    def drawTMouseMotion(screen, color, pointlist):
        mouse = pygame.mouse.get_pos()

        if (((mouse[0]< (pointlist[0][0]+5) )  or (mouse[0]> (pointlist[0][0]-5)) ) 
        and ((mouse[1]< pointlist[0][1]+5) or (mouse[1]> pointlist[0][1]-5) )
        ):
            print("Estamos aterrizando en el punto " + str(pointlist[0]))

        elif (((mouse[0]< pointlist[1][0]+5) or (mouse[0]> pointlist[1][0]-5) ) 
        and ((mouse[1]< pointlist[1][1]+5) or (mouse[1]> pointlist[1][1]-5) )
        ):
            print("Estamos aterrizando en el punto " + str( pointlist[1]))

        elif ((mouse[0]< pointlist[2][0]+5 or mouse[0]> pointlist[2][0]-5 ) 
        and ((mouse[1]< pointlist[2][1]+5) or (mouse[1]> pointlist[2][1]-5) )
        ):
            print("Estamos aterrizando en el punto " + str(pointlist[2]))
        else:
            print("Nos hemos pasao")

        




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

                #drawAxis(screenWH)
                pygame.draw.polygon(screen, color, pointlist, 1)

                if event.type == pygame.MOUSEMOTION:     
                    drawTMouseMotion(screen, color2, pointlist)

                pygame.display.flip()

                