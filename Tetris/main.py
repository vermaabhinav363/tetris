import pygame
import random
pygame.init()

screen=pygame.display.set_mode((600,792))

pygame.display.set_caption("Tetrix")
icon=pygame.image.load('box.png')
pygame.display.set_icon(icon)

sqImg=pygame.image.load('square.png')
pygame.display.set_icon(sqImg)

m = 27
n = 33

a = [[0 for x in range(n)] for x in range(m)]

class square1:

    sq1x = int(random.randint(24,776)/24)*24
    sq1y = 24
    r_cor=600-72
    l_cor=0
    d_cor=2
    u_cor=2
    length=2
    def get_rand(self):
        return random.randint(0,30)*24
    def sq1(self,x,y,turn):
        if turn ==0:
            screen.blit(sqImg, (x , y))
            screen.blit(sqImg, (x + 24, y))
            screen.blit(sqImg, (x + 48, y))
            screen.blit(sqImg, (x + 48, y+24))
        elif turn ==1:
            screen.blit(sqImg, (x+48, y-24))
            screen.blit(sqImg, (x + 24, y+24))
            screen.blit(sqImg, (x + 48, y))
            screen.blit(sqImg, (x + 48, y + 24))
        elif turn ==2:
            screen.blit(sqImg, (x+0, y+24))
            screen.blit(sqImg, (x + 0, y))
            screen.blit(sqImg, (x + 24, y+24))
            screen.blit(sqImg, (x + 48, y + 24))

        elif turn ==3:
            screen.blit(sqImg, (x+24, y+24))
            screen.blit(sqImg, (x + 24, y))
            screen.blit(sqImg, (x + 48, y-24))
            screen.blit(sqImg, (x + 24, y -24))

    def index(self,x,y,turn):
       if turn==0:
        a[int(x/24)][int(y/24)]=1
        a[int(x / 24)+1][int(y / 24)] = 1
        a[int(x / 24)+2][int(y / 24)] = 1
        a[int(x / 24)+2][int(y / 24)+1] = 1
       elif turn==1:
        a[int(x/24)+2][int(y/24)-1]=1
        a[int(x / 24)+1][int(y / 24)+1] = 1
        a[int(x / 24)+2][int(y / 24)] = 1
        a[int(x / 24)+2][int(y / 24)+1] = 1
       elif turn==2:
        a[int(x/24)][int(y/24)+1]=1
        a[int(x / 24)][int(y / 24)] = 1
        a[int(x / 24)+1][int(y / 24)+1] = 1
        a[int(x / 24)+2][int(y / 24)+1] = 1
       elif turn==3:
        a[int(x/24)+1][int(y/24)+1]=1
        a[int(x / 24)+1][int(y / 24)] = 1
        a[int(x / 24)+1][int(y / 24)-1] = 1
        a[int(x / 24)+2][int(y / 24)-1] = 1
    def is_down(self,x,y,turn):
        if turn==0:
            if a[int(x/24)][int(y/24)+1]==1 or a[int(x/24)+1][int(y/24)+1]==1 or a[int(x/24)+2][int(y/24)+2] ==1:
                return True
        elif turn==1:
            if a[int(x/24)+1][int(y/24)+2]==1 or a[int(x/24)+2][int(y/24)+2]==1:
                return True
        elif turn==2:
            if a[int(x/24)][int(y/24)+2]==1 or a[int(x/24)+1][int(y/24)+2]==1 or a[int(x/24)+2][int(y/24)+2]==1:
                return True
        elif turn==3:
            if a[int(x/24)+1][int(y/24)+2]==1 or a[int(x/24)+2][int(y/24)]==1:
                return True
    def is_right(self,x,y,turn):
        if turn==0:
            if a[int(x/24)+3][int(y/24)]==1 or a[int(x/24)+3][int(y/24)+1]==1:
                return False
        if turn==1:
            if a[int(x/24)+3][int(y/24)]==1 or a[int(x/24)+3][int(y/24)+1]==1 or a[int(x/24)+3][int(y/24)-1]==1:
                return False
        if turn==2:
            if a[int(x/24)+3][int(y/24)+1]==1 or a[int(x/24)+1][int(y/24)]==1:
                return False
        if turn==3:
            if a[int(x/24)+3][int(y/24)-1]==1 or a[int(x/24)+2][int(y/24)+0]==1 or a[int(x/24)+2][int(y/24)+1]==1:

                return False

        else:
            return True
    def is_left(self,x,y,turn):
        if a[int(x/24)-1][int(y/24)]==1:
            return False
        else:
            return True


square=square1()


running=True
logo=pygame.image.load('logo.png')
logox=250
logoy=350


turn =0
while running:


    screen.fill((255, 255, 255))
    screen.blit(logo, (logox, logoy))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and square.is_left(square.sq1x,square.sq1y,turn) :

               square.sq1x=square.sq1x-24

            if event.key == pygame.K_RIGHT and square.is_right(square.sq1x,square.sq1y,turn) :
                square.sq1x=square.sq1x+24
            if event.key == pygame.K_UP:
                turn=turn+1
                print(turn)
                turn=turn%4

        if event.type==pygame.KEYUP:
            pass
    if square.sq1x<0:
        square.sq1x=0
    if square.sq1x>square.r_cor:
        square.sq1x=square.r_cor
    square.sq1y=square.sq1y+0.1

    if(square.sq1y>792-square.u_cor*24 or square.is_down(square.sq1x,square.sq1y,turn)):
        square.index(square.sq1x,square.sq1y,turn)
        square=square1()
        square.sq1x=square.get_rand()
        square.sq1y = square.sq1y - 50

    square.sq1(square.sq1x,square.sq1y,turn)
    for i in range(25):
        for j in range(33):
            if a[i][j]==1:
                screen.blit(sqImg, (i*24, (j)*24))

    pygame.display.update()