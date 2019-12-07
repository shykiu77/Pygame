#!/usr/bin/env python3
import pygame, sys
from pygame.locals import *
from pygame import gfxdraw

FPS = 30
WINDOWNWIDTH = 640
WINDOWNHEIGHT = 640
TILEWIDTH = 80
TILEHEIGHT = 80
assert (WINDOWNWIDTH*WINDOWNHEIGHT)/(TILEWIDTH*TILEHEIGHT) == 64

WHITE = (250,250,250)
GREY = (128,128,128)
BROWN = (139,69,19)
BLACK = (5,5,5)

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWNWIDTH,WINDOWNHEIGHT))
pygame.display.set_caption('Checkers')

def DrawTiles(DISPLAYSURF):
    for i in range(0,8):
        for j in range(0,8):
            Rect = pygame.Rect(i*TILEWIDTH,j*TILEHEIGHT,TILEWIDTH,TILEHEIGHT)
            pygame.draw.rect(DISPLAYSURF,BROWN if (i+j)%2 !=0 else GREY,Rect)

def DrawPieces(board,DISPLAYSURF):
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j] != None:
                #pygame.draw.circle(DISPLAYSURF,board[i][j],(j*TILEWIDTH + (int) (TILEWIDTH/2),i*TILEHEIGHT+ (int)(TILEHEIGHT/2)),25)
                pygame.gfxdraw.aacircle(DISPLAYSURF,j*TILEWIDTH + (int) (TILEWIDTH/2),i*TILEHEIGHT+ (int)(TILEHEIGHT/2),25,board[i][j])
                #pygame.gfxdraw.filled_circle(DISPLAYSURF,j*TILEWIDTH + (int) (TILEWIDTH/2),i*TILEHEIGHT+ (int)(TILEHEIGHT/2),25,board[i][j])

def main():
    DISPLAYSURF.fill(WHITE)
    DrawTiles(DISPLAYSURF)
    board = []
    for i in range(0,8):
        line = []
        for j in range(0,8):
            if i <= 2 and (i+j)%2 != 0:
                line.append(WHITE)
            elif i >= WINDOWNWIDTH/TILEWIDTH - 3 and (i+j)%2 != 0:
                line.append(BLACK)
            else:
                line.append(None)
        board.append(line)
    
    DrawPieces(board,DISPLAYSURF)
    
    pygame.display.update()
    mousex = 0
    mousey = 0
   

    while True:
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex,mousey = event.pos
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
