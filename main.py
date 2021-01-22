from graph import Graph

def main():
    n=int(input("Enter dimensions of board"))
    g=Graph(n)

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

    g.DispAdj()

if __name__ == "__main__":
    main()