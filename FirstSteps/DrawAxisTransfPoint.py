import pygame


screenSize= [800, 600] #width height

def transPoint(p, c):
    """ This function receives the point "p" (array, point coord) and the weidht and height 
        of the screen "c" (array too), then, it returns the point transformed"""
 
 
    return (int( c[0]/2 +p[0]), int( c[1]/2 -p[1]))


def drawAxis(screen, screenSizes, color): 
    """ Receives the surface which the lines and dots are gonna be painted
    And the size of the surface [width, height] """
    pygame.draw.line(screen, color, [ screenSizes[0]/2, 0], [screenSizes[0]/2, screenSizes[1]]  , 2)
    pygame.draw.line(screen, color, [0, screenSizes[1]/2], [screenSizes[0], screenSizes[1]/2]  , 2)





if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(screenSize)
    pygame.display.flip()
    end = True
    color = (250, 40, 0)
    point = [50, 90]

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

            drawAxis(screen, screenSize, color)
            pygame.draw.circle(screen, color, transPoint(point, screenSize) , 1)

            pygame.display.flip() 

