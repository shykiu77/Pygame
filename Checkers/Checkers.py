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
            if (x + y) % 2 == 1 and board[x][y] != None:
                #pygame.draw.circle(DISPLAYSURF,board[i][j],(j*TILEWIDTH + (int) (TILEWIDTH/2),i*TILEHEIGHT+ (int)(TILEHEIGHT/2)),25)
                pygame.gfxdraw.aacircle(DISPLAYSURF,x*TILEWIDTH + (int) (TILEWIDTH/2),y*TILEHEIGHT+ (int)(TILEHEIGHT/2),25,board[x][y])
                pygame.gfxdraw.filled_circle(DISPLAYSURF,x*TILEWIDTH + (int) (TILEWIDTH/2),y*TILEHEIGHT+ (int)(TILEHEIGHT/2),25,board[x][y])

def getTilePos(mousexy):
    return ((int)(mousexy[0]/TILEWIDTH),(int)(mousexy[1]/TILEHEIGHT))

def CheckMovement(board, moving_piece, click_location):
    x, y = moving_piece
    j = 1
    
    if board[x][y] == BLACK:
        j = -1

    for i in (-1, 1):
        if click_location == (x + i, y + j):
            return True
        elif board[x + i][y + j] != board[x][y] and click_location == (x + (2 * i), y + (2 * j)):
            return True
    return False

def Move(board, moving_piece, click_location):
    x, y = moving_piece
    i, j = click_location
    board[i][j] = board[x][y]
    if board[(int)((x + i) / 2)][(int)((y + j) / 2)] != board[x][y]:
        board[(int)((x + i) / 2)][(int)((y + j) / 2)] = None
    board[x][y] = None
    return board

def main():
    DISPLAYSURF.fill(WHITE)
    DrawTiles(DISPLAYSURF)
    board = []
    for i in range(0,8):
        column = []
        for j in range(0,8):
            if (i+j)%2 == 0:
                column.append(GREY)
            elif j <= 2:
                column.append(WHITE)
            elif j >= WINDOWNWIDTH/TILEWIDTH - 3:
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
                if board[click_location[0]][click_location[1]] != GREY:
                    if board[click_location[0]][click_location[1]] != None:
                        if moving_piece == click_location:
                            moving_piece = None
                            moving = False
                        else:
                            moving_piece = click_location
                            moving = True
                        print('click ', click_location)
                    elif moving == True:
                        if CheckMovement(board, moving_piece, click_location):
                            board = Move(board, moving_piece, click_location)
                            DrawTiles(DISPLAYSURF)
                            DrawPieces(board, DISPLAYSURF)
                        removame = None
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
