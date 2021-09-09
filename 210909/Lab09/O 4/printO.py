
def showO(n):
    for _  in range(n):
        for a1 in range(1, (n+1)//2 + 1): #from row 1 to 5
            print(" "*((n+1)//2 - a1), end = "")
            for i in range(n):
                print("O"*((a1*2)-1), end = " "*(n-a1*2+1))
            print("")

        for a1 in range((n+1)//2 + 1, n + 1): #from row 6 to 9
            print(" "*(a1 - (n+1)//2), end = "")
            for i in range(n):
                print("O"*((n+1 - a1)*2 - 1), end = " "*(a1*2-n-1))
            print()
