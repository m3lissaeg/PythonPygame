import pygame

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([600, 600])
    pygame.display.flip()
    end = True    
    SALMON = (250, 128, 114)
    posY= 100
    posX = 100
    
    while end :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end= False

            while posY<1500:  
                #screen.fill((0,0,0))       to see the line moving, not drawing the complete path   
                pygame.draw.line(screen, SALMON, [100, 100], [500, posY], 2 )
                pygame.display.flip()
                posY = posY +1
                posX = posX -1

                
 
    """ if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            
        #print line        
        screen.fill([0, 0, 0])
        pygame.draw.line(screen, [200, 200, 0], [100, 100], pos , 2)
 """

