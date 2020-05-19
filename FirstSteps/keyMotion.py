import pygame

#TODO: Finish this  mouse moution exercise

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([600, 900])
    pygame.display.flip()
    color =  (250, 0, 250)
    end = True
    posY= 300
    posX = 450

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

            if event.type == pygame.KEYDOWN:
                pos= pygame.mouse.get_pos()
                pygame.draw.circle(screen, color, pos, 15)
                pygame.display.update()     


