import pygame, sys
from pygame.locals import *

FPS = 30
WINDOWNWIDTH = 640
WINDOWNHEIGHT = 640
TILEWIDTH = 80
TILEHEIGHT = 80
assert (WINDOWNWIDTH*WINDOWNHEIGHT)/(TILEWIDTH*TILEHEIGHT) == 64

WHITE = (255,255,255)
GREY = (128,128,128)
BROWN = (139,69,19)
BLACK = (0,0,0)

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWNWIDTH,WINDOWNHEIGHT))
pygame.display.set_caption('Checkers')

def DrawTiles(DISPLAYSURF):
    for i in range(0,8):
        for j in range(0,8):
            Rect = pygame.Rect(i*TILEWIDTH,j*TILEHEIGHT,TILEWIDTH,TILEHEIGHT)
            pygame.draw.rect(DISPLAYSURF,BROWN if (i+j)%2 ==0 else GREY,Rect)

def main():
    DISPLAYSURF.fill(WHITE)
    DrawTiles(DISPLAYSURF)
    pygame.display.update()
    
    board = []
    for i in range(0,8):
        line = []
        for j in range(0,8):
            if i <= 1:
                line.append(WHITE)
            elif i >= WINDOWNWIDTH/TILEWIDTH - 2:
                line.append(BLACK)
            else:
                line.append(None)
        board.append(line)
    
    for i in range(0,8):
        for j in range(0,8):
            print(board[i][j])
        print('\n')
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    
if __name__ == '__main__':
    main()
