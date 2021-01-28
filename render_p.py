import soln, board, time
from board import board
import sys, pygame
pygame.init()

WIDTH=750
HEIGHT=820
BGC=(28,170,156)
LINE_COLOR=(255,255,255)
WHITE=(255,255, 255)
RED=(255,0,0)
St=15
En=735
TXCOL=(0,0,255)
NUMCOL=(0,0,0)
WRONG=(255,0,0)
OFST=36


def draw_bg():
    screen.fill(BGC)
    pygame.draw.rect(screen, pygame.Color("Black"), pygame.Rect(15,15,720,720), 6)

    for i in range(9):
        if i%3==0:
            t=4
        else:
            t=1
        pygame.draw.line(screen, pygame.Color("Black"), (i*80+15 , St), (i*80 +15 ,En), t )
        pygame.draw.line(screen, pygame.Color("Black"), (St , i*80+15), (En ,i*80+15), t )


def draw_num(bd):
    row=0
    while row<9:
        col=0
        while col<9:
            output=bd[row][col]
            if output != 0:
                n_text= font.render(str(output), True, TXCOL)
                screen.blit(n_text, (col*80+OFST+4, row*80+OFST))
            col+=1
        row+=1

def is_avail(row, col):
    if board[row][col]==0:
        return True

    return False

def mark_square(row, col):
    screen.fill((0, 255, 0))
    pygame.draw.rect(screen, WHITE, pygame.Rect(10,10,30,30), 6)
    print(row,col)


def place(row, col, key):
    if board[row][col]!=0:
        return
    
    if soln.solve(board):
        board[row][col]=key
        print(key)
        n_text= font.render(str(key), True, TXCOL)
        #print(n_text)
        screen.blit(n_text, (col*80+OFST+4, row*80+OFST))

    elif not soln.isvalid(board, key, (row,col)) :
        n_text2= font.render(str(key), True, WRONG)
        print(key)
        #print(n_text)
        screen.blit(n_text2, (col*80+OFST+4, row*80+OFST))






screen = pygame.display.set_mode((WIDTH,HEIGHT))  #(wxh)
pygame.display.set_caption("Sudoku ")
font=pygame.font.SysFont(None, 70)

key = None
run = True
start = time.time()
strikes = 0
game_over=False

#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Close button works
            sys.exit()
    #pygame.display.flip()
        draw_bg()
        draw_num(board)
        pygame.display.update()

        if event.type== pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX=event.pos[0]
            mouseY=event.pos[1]

            clk_row=mouseY//80
            clk_col=mouseX//80

            if is_avail(clk_row, clk_col):
                mark_square(clk_row, clk_col)
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                key = 1
            if event.key == pygame.K_2:
                key = 2
            if event.key == pygame.K_3:
                key = 3
            if event.key == pygame.K_4:
                    key = 4
            if event.key == pygame.K_5:
                key = 5
            if event.key == pygame.K_6:
                key = 6
            if event.key == pygame.K_7:
                key = 7
            if event.key == pygame.K_8:
                key = 8
            if event.key == pygame.K_9:
                key = 9
            if event.key == pygame.K_DELETE:
                board.clear()
                key = None

            place(clk_row, clk_col, key)
            
                    #if check_win(player):
                     #   game_over=True

                    #player=player%2+1
                    #draw_fig()
