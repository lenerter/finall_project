import pygame    
import random
import time

print("Looading.")
time.sleep(1)
print("Looading..")
time.sleep(1)
print("Looading...")
time.sleep(1)
print("-=-=-starting-=-=-")
pygame.init()
FPS=7
fpsClock=pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))
bg_color = (255, 255, 255)
screen.fill(bg_color)

wall = pygame.image.load('wall.png').convert_alpha()
air = pygame.image.load('air.png').convert_alpha()
player = pygame.image.load('player.png').convert_alpha()
win = pygame.image.load('win.png').convert_alpha()
finalbg = pygame.image.load('finalbg.png').convert_alpha()
fall = pygame.image.load('fall.png').convert_alpha()
bad = pygame.image.load('bad.png').convert_alpha()
key = pygame.image.load('key.png').convert_alpha()
sword = pygame.image.load('sword.png').convert_alpha()

in_file = open('maps.txt').read().splitlines()
maps = [[int(cell) for cell in line.split()] for line in in_file]
bg=0
stop=1
cast=0
start=1
kl=0

while True:
    fpsClock.tick(FPS)
    pygame.display.flip()
    
    for i in range(10):
        for j in range(10):
            if maps[i][j] == 0:
                screen.blit(air, (i*50, j*50))
            elif maps[i][j] == 1:
                screen.blit(player, (i*50, j*50))
                x=i
                y=j
            elif maps[i][j] == 2:
                screen.blit(wall, (i*50, j*50))
            elif maps[i][j] == 3:
                screen.blit(win, (i*50, j*50))
            elif maps[i][j] == 4:
                screen.blit(bad, (i*50, j*50))
                bx=i
                by=j
            elif maps[i][j] == 5:
                screen.blit(key, (i*50, j*50))
    
    rnd = random.randint(1,4)
    if rnd == 1:
        if maps[bx-1][by] == 2:
                pass
        elif maps[bx-1][by] == 5:
               pass
        elif maps[bx-1][by] == 3:
            maps[bx][by]=0
            bg = 2
        elif maps[bx-1][by] == 1:
            maps[bx][by]=0
            bg = 2
        else:
            maps[bx][by]=0
            maps[bx-1][by]=4
            
    if rnd == 2:
        if maps[bx+1][by] == 2:
                pass
        elif maps[bx+1][by] == 5:
                pass
        elif maps[bx+1][by] == 3:
            maps[bx][by]=0
            bg = 2
        elif maps[bx+1][by] == 1:
            maps[bx][by]=0
            bg = 2
        else:
            maps[bx][by]=0
            maps[bx+1][by]=4
    if rnd == 3:
        if maps[bx][by-1] == 2:
                pass
        elif maps[bx][by-1] == 5:
                pass
        elif maps[bx][by-1] == 3:
            maps[bx][by]=0
            bg = 2
        elif maps[bx][by-1] == 1:
            maps[bx][by]=0
            bg = 2
        else:
            maps[bx][by]=0
            maps[bx][by-1]=4
    if rnd == 4:
        if maps[bx][by+1] == 2:
                pass
        elif maps[bx][by+1] == 5:
                pass
        elif maps[bx][by+1] == 3:
            maps[bx][by]=0
            bg = 2
        elif maps[bx][by+1] == 1:
            maps[bx][by]=0
            bg = 2
        else:
            maps[bx][by]=0
            maps[bx][by+1]=4
    


    if bg == 1:
        if stop == 1:
            screen.blit(finalbg, (0, 0))
            cast=1
            stop=0
        else:
            pass
        
    elif bg == 2:
        if stop == 1:
            secret = random.randint(1,100)
            if secret == 67:
                screen.blit(sword, (0, 0))
            else:
                screen.blit(fall, (0, 0))
            cast=2
            stop=0
        else:
            pass
    if  cast == 1:
        screen.blit(finalbg, (0, 0))
    elif cast == 2:
        screen.blit(fall, (0, 0))
    else:
        pass
            
 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if start == 1:
                    if maps[x-1][y] == 2:
                        pass
                    elif maps[x-1][y] == 3:
                        if kl == 1: 
                            maps[x][y]=0
                            bg = 1
                        else:
                            pass
                    elif maps[x-1][y] == 4:
                        maps[x][y]=0
                        bg = 2
                    elif maps[x-1][y] == 5:
                        maps[x][y]=0
                        maps[x-1][y]=1
                        kl=1
                    else:
                        maps[x][y]=0
                        maps[x-1][y]=1
                    start=1
                else:
                    pass
            elif event.key == pygame.K_RIGHT:
                if start == 1:
                    start=0
                    if maps[x+1][y] == 2:
                        pass
                    elif maps[x+1][y] == 3:
                        if kl == 1:
                            maps[x][y]=0
                            bg = 1
                        else:
                            pass
                    elif maps[x+1][y] == 4:
                        maps[x][y]=0
                        bg = 2
                    elif maps[x+1][y] == 5:
                        maps[x][y]=0
                        maps[x+1][y]=1
                        kl=1
                    else:
                        maps[x][y]=0
                        maps[x+1][y]=1
                    start=1
                else:
                    pass
            elif event.key == pygame.K_UP:
                if start == 1:
                    start=0
                    if maps[x][y-1] == 2:
                        pass
                    elif maps[x][y-1] == 3:
                        if kl == 1:
                            maps[x][y]=0
                            bg = 1
                        else:
                            pass
                    elif maps[x][y-1] == 4:
                        maps[x][y]=0
                        bg = 2
                    elif maps[x][y-1] == 5:
                        maps[x][y]=0
                        maps[x][y-1]=1
                        kl=1
                    else:
                        maps[x][y]=0
                        maps[x][y-1]=1
                    start=1
                else:
                    pass
            elif event.key == pygame.K_DOWN:
                if start == 1:
                    start=0
                    if maps[x][y+1] == 2:
                        pass
                    elif maps[x][y+1] == 3:
                        if kl == 1:
                            maps[x][y]=0
                            bg = 1
                        else:
                            pass
                    elif maps[x][y+1] == 4:
                        maps[x][y]=0
                        bg = 2
                    elif maps[x][y+1] == 5:
                        maps[x][y]=0
                        maps[x][y+1]=1
                        kl=1
                    else:
                        maps[x][y]=0
                        maps[x][y+1]=1
                    start=1
                else:
                    pass
            
