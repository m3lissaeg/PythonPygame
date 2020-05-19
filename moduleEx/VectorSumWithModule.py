import pygame
import DrawAxisTransfPoint  as AP

#HEIGH = 600
#WIDTH = 800

    

def vectorSum(a, b):
    c=[]
    i=0
    for i in range(len(a)):
        c.append(a[i]+b[i])

    return c 

 # --------- main --------------------------

if __name__ == '__main__':
    pygame.init()
    end = True

   
    screen = pygame.display.set_mode(AP.screenSize)
     
    pygame.display.flip()
    SALMON = (250, 128, 114)
    color = (200, 210, 100)
    end = True    
    posY= 100
    posX = 100
    point = [50, 90]
    point1 = [100,120]
    point2 = [40,80]

    while end :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end= False
           
            AP.drawAxis(screen, AP.screenSize, color)
            pygame.draw.circle(screen, color, AP.transPoint(point, AP.screenSize) , 1)

            centerPoint = AP.transPoint([0,0], AP.screenSize )
            pygame.draw.line(screen, color,centerPoint , AP.transPoint(point1, AP.screenSize), 2)
            pygame.draw.line(screen, color,centerPoint, AP.transPoint(point2, AP.screenSize), 2)
            pygame.draw.line(screen, SALMON, centerPoint, AP.transPoint(vectorSum(point1, point2), AP.screenSize ), 2)
            pygame.display.flip()
