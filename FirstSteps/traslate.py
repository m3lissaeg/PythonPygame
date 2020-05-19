import pygame


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


    def trasPoint(p, d):
        """ This function receives the line "p" (array) and the displacement in te x and y axis (array too),
            then, it returns the point traslated"""

        return ([d[0] + p[0], d[1] + p[1]])

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

            drawAxis(screenWH)

            tPoint = trasPoint(point1, (50,0))
            pygame.draw.circle(screen, color, point1,  1)
            pygame.draw.circle(screen, color, tPoint,  1)
            pygame.display.flip()
            
          

