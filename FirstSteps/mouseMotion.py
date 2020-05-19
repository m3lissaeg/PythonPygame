import pygame

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode([800, 500])
    pygame.display.flip()
    end = True

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

            if event.type == pygame.MOUSEMOTION:
                print (event.pos)
    


