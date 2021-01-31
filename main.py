from graph import Graph
import math, soln, time
from board import *

def main():
    
    ch=input("enter 1 if you want to create custom puzzle, or 2 to solve random 9x9 puzzle: ")

    if ch=='2':
        n=9
        board=board_diff
    elif ch=='1':
        n=int(input("Enter dimensions of board"))
        g=Graph(n)
        board = [[0 for x in range(n)] for y in range(n)]
        while True:
            print("enter row, col, number")
            try:
                x=int(input())
                y=int(input())
                num=int(input())
                if x>n or y>n or num>n:
                    break
                g.AddEdge(x,y,num)

            except Exception as e:
                print(e)
                break

        g.GraphtoBoard(board)
        #print(len(board))
    disp_board(board)

    sl=int(input("enter 1 if you want to run backtrack, 2 to run fwd check: "))
    start = time.time()
    
    if sl==1:
        soln.sol_fwd_check(board)
    else:
        soln.solve(board)
    
    end = time.time()

    disp_board(board)
    print(f"Runtime of the program is {end - start}")
        

if __name__ == "__main__":
    main()