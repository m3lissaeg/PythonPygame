import pygame


HEIGH = 600
WIDTH = 900
SALMON = (250, 128, 114)
NEGRO = [0,0,0]

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([900, 600]) # width   heigh
    pygame.display.flip()
    color =  (250, 0, 250)
    end = True
    posx= 20
    posy = 20
    speedX =0
    speedY=0
    clk = pygame.time.Clock()

    img= pygame.image.load('/home/melii/Documents/Python/game/img.png')
    screen.blit(img, [posx, posy])
    pygame.display.flip()

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    speedX = 2

                if event.key == pygame.K_LEFT:
                    speedX = -2 

                if event.key == pygame.K_DOWN:
                    speedY = 2 

                if event.key == pygame.K_UP:
                    speedY = -2    

            
            screen.fill(NEGRO)
            posx += speedX
            posy += speedY
            print(posx, posy)
            screen.blit(img, [posx, posy])
            pygame.display.flip()

            #clk.tick(30)
