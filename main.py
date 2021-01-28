from graph import Graph
import math, soln
from board import *

def main():
    
    ch=input("enter 1 if you want to create custom puzzle, 2 to solve random 9x9 puzzle: ")

    if ch=='2':
        n=9
        board=[[0 for x in range(n)] for y in range(n)]
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

    soln.solve(board)
    disp_board(board)
        

if __name__ == "__main__":
    main()