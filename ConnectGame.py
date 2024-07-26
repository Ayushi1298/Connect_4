import numpy as np
import sys
import math
import pygame

Blue=(0,0,255)
Black=(0,0,0)
Red=(255,0,0)
Yellow=(255,255,0)
Peach2=(255,213,145)
row_count=6
column_count=7

def create_board():
    board=np.zeros((row_count,column_count))
    return board
def drop_piece(board,row,col,piece):
    board[row][col]=piece


def is_valid_location(board,col):
    return board[row_count-1][col]==0
def get_next_open_row(board,col):
    for r in range(row_count):
        if board[r][col]==0:
            return r
def print_board(board):
    print(np.flip(board,0))
def winning_move(board,piece):

    #Horizontal Winner
    for c in range(column_count-3):
        for r in range(row_count):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True

    #Vertical winner
    for c in range(column_count):
        for r in range(row_count-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True

    #Positive Slope Winner
    for c in range(column_count-3):
        for r in range(row_count-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True

    #Negative Slope Winner
    for c in range(column_count-3):
        for r in range(3,row_count):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True


def draw_board(board):
    for c in range(column_count):
        for r in range(row_count):
            pygame.draw.rect(screen,Peach2,(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen, Black, (int(c * SQUARESIZE+ SQUARESIZE/2), int(r*SQUARESIZE+ SQUARESIZE + SQUARESIZE/2)),radius)
    for c in range(column_count):
        for r in range(row_count):

            if board[r][c] == 1:
                pygame.draw.circle(screen, Red, (int(c * SQUARESIZE+ SQUARESIZE/2), height- int(r*SQUARESIZE+ SQUARESIZE/2)),radius)
            elif board[r][c]==2:
                pygame.draw.circle(screen, Blue, (int(c * SQUARESIZE + SQUARESIZE/2), height- int(r * SQUARESIZE + SQUARESIZE/2)), radius)
    pygame.display.update()


board=create_board()
print_board(board)
game_over=False
turn=0

pygame.init()

SQUARESIZE=100
width=column_count*SQUARESIZE
height=(row_count+1)*SQUARESIZE
size=(width,height)
radius=int(SQUARESIZE/2-5)
screen=pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

font_style=pygame.font.SysFont("monospace",75)

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            pygame.draw.rect(screen,Black,(0,0,width,SQUARESIZE))
            posx=event.pos[0]
            if turn==0:
                pygame.draw.circle(screen,Red,(posx,int(SQUARESIZE/2)),radius)
            else:
                pygame.draw.circle(screen, Blue, (posx, int(SQUARESIZE / 2)), radius)
        pygame.display.update()

        if event.type==pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,Black, (0, 0, width, SQUARESIZE))

            #Player 1
            if turn==0:
                posx=event.pos[0]
                col=int(math.floor(posx/SQUARESIZE))
                if is_valid_location(board,col):
                    row=get_next_open_row(board,col)
                    drop_piece(board,row,col,1)
                    if winning_move(board,1):
                        label=font_style.render("Player 1 wins!",1,Red)
                        screen.blit(label,(40,10))
                        game_over=True

            #Player 2
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    if winning_move(board, 2):
                        label = font_style.render("Player 2 wins!", 1, Yellow)
                        screen.blit(label, (40, 10))
                        game_over = True

            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)