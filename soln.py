import math
def findEmpty(bd):
    n=len(bd)
    for i in range(n):
        for j in range(n):
            if bd[i][j]==0:
                return (i,j)

    return None

def isvalid(bd, num, pos):
    #num is the number entered, pos is a tuple (x, y) poitning to an empty position
    n=len(bd)
    rn=int(math.sqrt(n))
    #checking row and column
    for i in range (n):
        if bd[pos[0]][i]==num and i!= pos[1]:
            return False

        if bd[i][pos[1]]==num and i!=pos[0]:
            return False

        
    block_x=int(pos[1]//rn)
    block_y=int(pos[0]//rn)
    for i in range(block_y*rn, block_y*rn+rn):
        for j in range(block_x*rn, block_x*rn +rn):
            if bd[i][j]==num and (i,j) != pos:
                return False
    
    return True


def solve(bd):
    find = findEmpty(bd)

    if not find:
        return True

    else: 
        r, c = find

    for i in range(1, len(bd)+1):
        if isvalid(bd, i, (r,c)):
            bd[r][c]=i

            if solve(bd):
                return True

            bd[r][c]=0

    return False

dom=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
domain=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

def in_dom(i):
    if i in domain:
        return True
    else:
        return False

def sol_fwd_check(bd):
    global domain
    find = findEmpty(bd)

    if not find:
        return True

    else: 
        r, c = find

    for i in range(1, len(bd)+1):
        if in_dom(i) and isvalid(bd, i, (r,c)):
            bd[r][c]=i
            domain.remove(i)

            if solve(bd):
                return True

            bd[r][c]=0
            domain=dom

    return False