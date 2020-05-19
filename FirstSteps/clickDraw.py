import pygame

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode([900, 600])
    pygame.display.flip()
    end = True
    color =  (250, 0, 250)
    pos =()
    

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

            if event.type == pygame.MOUSEBUTTONDOWN:                      
                pygame.draw.line(screen, color, [100, 100], event.pos , 2)
                pygame.display.flip()

            

