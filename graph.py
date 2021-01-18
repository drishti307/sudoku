class Graph:
    __n=0
    __adj = [[0 for x in range(10)] for y in range(10)]

    def __init__(self, x):
        print("graph initialised")
        self.__n=x
        
        for i in range(self.__n): 
            for j in range(self.__n): 
                self.__adj[i][j]=0

    def AddEdge(self, x, y, p):
        if (x-1 >= self.__n) or (x<= 0) or (y-1>self.__n) or (y<=0):
            return -1
        
        elif x==y:
            self.__adj[x-1][y-1]=p

        else:
            self.__adj[x-1][y-1]=p

        return self

    def DispAdj(self):
        print("Adjacency Matrix is: \n")
        for i in range(0, self.__n):
            for j in range(0, self.__n): 
                print("", self.__adj[i][j], end="") 
            print('\n') 

