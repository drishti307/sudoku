
def findEmpty(bd):
    n=len(bd)
    for i in range(n):
        for j in range(n):
            if bd[i][j]==0:
                return (i,j)

    return None

def isvalid(bd, num, pos):
    #num is the number entered, pos is a tuple (x, y) poitning to an empty position

    #checking row and column
    for i in range (len(bd)):
        if bd[pos[0]][i]==num and i!= pos[1]:
            return False

        if bd[i][pos[1]]==num and i!=pos[0]:
            return False

        
    block_x=pos[0]//3
    block_y=pos[1]//3

    for i in range(block_y*3, block_y*3 +3):
        for j in range(block_x*3, block_x*3 +3):
            if bd[i][j]==num and (i,j) != pos:
                return False

    
    return True


def solve(bd):
    find = findEmpty(bd)

    if not find:
        return True

    else: 
        r, c = find

    for i in range(1, 10):
        if isvalid(bd, i, find):
            bd[r][c]=i

            if solve(bd):
                return True

            bd[r][c]=0

    return False
