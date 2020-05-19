import pygame
import random


#TODO: hacer que lso enemigos disparen :)
#TODO: hacer que las bombas funcionen
#TODO: colision de las balas enemigas con el jugador
#TODO: qué pasa con el jugador? muere? recupera la salud?Agregar entonces modficadorpara la salud
#TODO: juego para dos jugadores :)
#TODO: al implementar choque en x y y , hay que evaluar is la vel es a la derecha o a la izquierda - con los bloques . Evaluar si el objeto hacia donde se esta moviendo


ANCHO=640
ALTO=480
ROJO=[255,0,0]
NEGRO=[0,0,0]
BLANCO=[255,255,255]
VERDE=[0,255,0]
SALMON = (240, 30, 100)
AZUL = (0,0, 200)
class Cuadro(pygame.sprite.Sprite):
    '''
    Clase cuadro
    '''
    def __init__(self, p , cl):
        pygame.sprite.Sprite.__init__(self)

        #self.id = =id
        self.image = pygame.Surface([40,50])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=0
        self.vely=0

        self.bombas = 0 
        self.vidas = 3
        self.salud = 3 # con cada bala la salud se decrementa, al final, cuando es cero, se resta 1 a la vida

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely



class Rival(pygame.sprite.Sprite):
    '''
    Clase rival
    '''
    def __init__(self, p , cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,40])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=5
        #self.vely=3
        self.temp = 100 #temporizador

    def update(self):
        self.rect.x += self.velx
        #self.rect.y += self.vely
        if self.temp >0 :
            self.temp -= 1  #Inicializr de nuevo el temp y disparar no s algo que se hará dentro de la clase, si no por fuera

class Bala(pygame.sprite.Sprite):
    '''
    Clase Bala
    '''
    def __init__(self, p , cl=ROJO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,20])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.vely=-7
        self.vely=3

    def update(self):
        self.rect.y += self.vely

class Bomba(pygame.sprite.Sprite):
    '''
    Clase Bomba
    '''
    def __init__(self, p , cl=ROJO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.vely=-5
        #self.vely=3

    def update(self):
        self.rect.y += self.vely

# ------------ Clase bloques ----

class Bloque(pygame.sprite.Sprite):
    '''
    Clase Bloque
    '''
    def __init__(self, p , cl=AZUL):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.vely=-5
        #self.vely=3

    def update(self):
        self.rect.y += self.vely



#-------------------------------------------------------------------------------------------------

class Ventaja(pygame.sprite.Sprite):
    '''
    Clase ventaja - modificadores 
    '''
    def __init__(self, p , cl=AZUL):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([8,8])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.vely=-5
        #self.vely=3

    def update(self):
        self.rect.y += self.vely

        if self.rect.y >= (ANCHO - self.rect.height):
            self.rect.y = ANCHO - self.rect.height
            self.vely = 0



if __name__ == '__main__':
    pygame.init()
    ptos=0
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    reloj=pygame.time.Clock()
    fin=False
    endGame = False

    jugadores= pygame.sprite.Group()
    rivales = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    balasR = pygame.sprite.Group()  #balas de los rivales
    bomba = pygame.sprite.Group()
    ventajas = pygame.sprite.Group()

    j1=Cuadro([100,100],VERDE)

    jugadores.add(j1)


    #Bloques
    bloques = pygame.sprite.Group()
    bl = Bloque ([300, 200], [100,  50])
    bloques.add(bl)

    #Letra

    fuente = pygame.font.Font(None, 33)
    texto = fuente.render('Inicio del juego', True, BLANCO)

    #creacion de rivales
    n=10
    for i in range(n):
        r=Rival([20,20])
        r.rect.x = random.randrange(1,150)
        r.rect.y = random.randrange(ALTO- (r.rect.height+100))
        r.velx = random.randrange(10)
        rivales.add(r)


    if event.type  == pygame.KEYDOWN:
       if event.key == pygame.K_RIGHT:
               j1.velx = 5
               j1.vely = 0
       if event.key == pygame.K_LEFT:
               j1.velx = -5
               j1.vely = 0
       if event.key == pygame.K_UP:
               j1.vely = -5
               j1.velx = 0
       if event.key == pygame.K_DOWN:
               j1.vely = 5
               j1.velx = 0
       if event.key == pygame.K_p:
               #crear balas
               b=Bala([j1.rect.x , j1.rect.y])
               balas.add(b)
       if event.key == pygame.K_i:
               #crear bomba
               u=Bomba([j1.rect.x , j1.rect.y])
               bomba.add(u)
       
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
                j1.velx=0
                j1.vely=0
        if event.key == pygame.K_LEFT:
                j1.velx=0
                j1.vely=0
        if event.key == pygame.K_UP:
                j1.velx=0
                j1.vely=0
        if event.key == pygame.K_DOWN:
                j1.velx=0
                j1.vely=0
        



        #control
        jugadores.update()

        #Agrega las condiciones de parada
        if j1.rect.x > (ANCHO - j1.rect.width):
            j1.rect.x = ANCHO - j1.rect.width
            j1.velx=0
        if j1.rect.x < (0):
            j1.rect.x = 0
            j1.velx=0
        if j1.rect.y > (ALTO - j1.rect.height):
            j1.rect.y = ALTO - j1.rect.height
            j1.vely=0
        if j1.rect.y < (0):
            j1.rect.y = 0
            j1.vely=0

        for r in rivales:
            if r.rect.x > (ANCHO - r.rect.width):
                r.velx = r.velx*-1
            if r.rect.x <= 0:
                r.velx = r.velx*-1

            if r.temp<= 0:
                b = Bala([r.rect.x , r.rect.y ], SALMON)
                b.vely = 7
                balasR.add(b)
                b.temp = random.randrange(100)




        #Se usa para que el grupo "balas" cuando choque con rivales, los elimine
        #Si se pone False, en vez de true, no lo elimina
        #Ejemplo: cuando un jugador esta en fuego que se queme
        for b in balas:
            ls_col=pygame.sprite.spritecollide(b,rivales,True)
            for r in ls_col:
                #SI es True, cuenta cuantos cuadros a eliminado
                ptos+=1    #la ventaja aparece cuando se haya golpeado un enemigo

                ifVentaja = random.randrange(1000)
                if ifVentaja > 800:
                    #crear ventaja
                    v = Ventaja ([r.rect.x , r.rect.y ])
                    ventajas.add(v)

                print (ptos)
                balas.remove(b)

        #Que sucede cuando el jugador toca una bala del rival? :

        for b in balasR:
            ls_col=pygame.sprite.spritecollide(b,jugadores,True)
            if j in ls_col:

                if j.vidas == 0:
                    endGame = True
                else : # collide lo elimina de la pantalla , por eso debo hacerlo aparecer de nuevo
                    if j.salud < 0:
                        j.salud -= 1

                    else : #si salud es menor a cero, se debe decrementar la cantidad de vidas que tiene el jugador
                        vACtual=  j.vidas  -1
                        j1 = Cuadro([100, 200] , VERDE)
                        j1.vidas = vACtual
                        jugadores.add(j1)
            


        for u in bomba:
            ls_col=pygame.sprite.spritecollide(u,rivales,True)
            for r in ls_col:
                bomba.remove(rivales)


        for j in jugadores:
            lsCap = pygame.sprite.spritecollide(j, ventajas, True)

            for v in lsCap:
                j.bombas += 1
                ventajas.remove(v)

        #Bloques
        for bl in bloques:
            ls = pygame.sprite.spritecollide(j1, bloques, False)
            for e in ls:
                if j1.rect.right > e.rect.left:
                    j1.rect.right = e.rect.left
                    j1.velx = 0

                if j1.rect.left < e.rect.right:
                    j1.rect.left = e.rect.right
                    j1.velx = 0    

                if j1.rect.bottom > e.rect.top:
                    j1.rect.bottom = e.rect.top
                    j1.vely = 0  

                if j1.rect.top > e.rect.bottom:
                    j1.rect.top = e.rect.bottom
                    j1.vely = 0  
                


        #limpieza
        for b in balas:
            if b.rect.y < -10:
                balas.remove(b)

        rivales.update()
        balas.update()
        bomba.update()
        ventajas.update()
        balasR.update()

        #refresca la pantala
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        balas.draw(pantalla)
        bomba.draw(pantalla)
        ventajas.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)

    while not (fin or endGame): #TODO: mejorar letra
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            #letra
            pantalla.fill(NEGRO)
            texto = fuente.render('Fin del juego', False, BLANCO)
            pantalla.blit( texto, [100, 100])
        


