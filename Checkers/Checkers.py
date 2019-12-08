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
    for x in range(0,8):
        for y in range(0,8):
            if board[x][y] != None:
                #pygame.draw.circle(DISPLAYSURF,board[i][j],(j*TILEWIDTH + (int) (TILEWIDTH/2),i*TILEHEIGHT+ (int)(TILEHEIGHT/2)),25)
                pygame.gfxdraw.aacircle(DISPLAYSURF,x*TILEWIDTH + (int) (TILEWIDTH/2),y*TILEHEIGHT+ (int)(TILEHEIGHT/2),25,board[x][y])
                pygame.gfxdraw.filled_circle(DISPLAYSURF,x*TILEWIDTH + (int) (TILEWIDTH/2),y*TILEHEIGHT+ (int)(TILEHEIGHT/2),25,board[x][y])

def getTilePos(mousexy):
    return ((int)(mousexy[0]/TILEWIDTH),(int)(mousexy[1]/TILEHEIGHT))

def main():
    DISPLAYSURF.fill(WHITE)
    DrawTiles(DISPLAYSURF)
    board = []
    for i in range(0,8):
        column = []
        for j in range(0,8):
            if j <= 2 and (i+j)%2 != 0:
                column.append(WHITE)
            elif j >= WINDOWNWIDTH/TILEWIDTH - 3 and (i+j)%2 != 0:
                column.append(BLACK)
            else:
                column.append(None)
        board.append(column)
    
    DrawPieces(board,DISPLAYSURF)
    
    pygame.display.update()
    moving_piece = (None,None)
    moving = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                click_location = getTilePos(event.pos)
                if board[click_location[0]][click_location[1]] != None:
                    moving_piece = click_location
                    moving = True
                elif moving == True:
                    removame = None
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
