import pygame
from math import radians, cos, sin 

ANCHO = 600
ALTO = 500

color = (20, 30, 40)

def drawAxis(screen, screenSizes, color): 
    """ Receives the surface which the lines and dots are gonna be painted
    And the size of the surface [width, height] """
    pygame.draw.line(screen, color, [ screenSizes[0]/2, 0], [screenSizes[0]/2, screenSizes[1]]  , 2)
    pygame.draw.line(screen, color, [0, screenSizes[1]/2], [screenSizes[0], screenSizes[1]/2]  , 2)



def drawCardioide(v) :
    """ r es el radio, angle es el angulo  """

    return [ v[0] * cos(v[1]) , v[0] * sin(v[1]) ]



def transLine(p, c):
    """ This function receives the line "p" (array) and the weidht and height of the screen "c" (array too),
       then, it returns the line transformed"""

    return [int(c[0]/2 +p[0]), int (c[1]/2 -p[1])]



if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    c=[300,250]
    drawAxis(pantalla,[600, 500], color)


    an=0
    an_p=100
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    an_p+=50
                    an=0
        
        ar= radians(an)
        r=an_p*(1+ cos(ar))

        #print r,an
        p= drawCardioide([r,an])
        pc=transLine(c,p)

        pygame.draw.line(pantalla, color, c , pc , 2)

        #Punto(pantalla,pc, VERDE)
        if an <= 360:
            an+=1
        pygame.display.flip()
