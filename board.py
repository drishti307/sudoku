from graph import Graph
import math

#default board
board=[
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,]
]


def disp_board(bd):
    n=len(bd)
    rn=math.sqrt(n)
    for i in range(n):
        if i%rn==0 and i!=0:
            print ("---------------------------")
        for j in range(n):
            if j%rn==0 and j!=0:
                print(" | ",  end="")
            print(str(bd[i][j])+" ", end="")

        print("\n")