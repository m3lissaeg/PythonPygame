import pygame

HEIGH = 600
WIDTH = 800

def drawCP(screen, c ):
    pygame.draw.line(screen, color, [c[0], 0], [c[0], HEIGH])
    pygame.draw.line(screen, color, [0, c[1]], [WIDTH, c[1]])
    pygame.display.flip()
    

def transformP(c, p):
    return [p[0]+c[0], -p[1]+c[1]]


def vectorSum(a, b):
    c=[]
    i=0
    for i in range(len(a)):
        c.append(a[i]+b[i])

    return c 

 # --------- main --------------------------

if __name__ == '__main__':
    pygame.init()

   
    screen = pygame.display.set_mode([WIDTH, HEIGH])
    c= [int(WIDTH/2), int(HEIGH/2)]
    color = (0, 150, 150)
    colorS = (250, 0, 0)
    
    pygame.display.flip()
    end = True    
    SALMON = (250, 128, 114)
    posY= 100
    posX = 100
    
    while end :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end= False
            
            point1 = [100,120]
            point2 = [40,80]
            drawCP(screen, c )
            pygame.draw.line(screen, color, transformP(c,[0,0]), transformP(c, point1), 2)
            pygame.draw.line(screen, color, transformP(c,[0,0]), transformP(c, point2), 2)
            pygame.draw.line(screen, colorS, transformP(c,[0,0]), transformP(c, vectorSum(point1, point2)), 2)
            pygame.display.flip()
