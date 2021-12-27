atoz = [chr(i) for i in range(ord("a"),ord("z")+1)]
AtoZ = [chr(i) for i in range(ord("A"),ord("Z")+1)]
#inp = "privatekey1.txt"
inp2 = input("Enter publickey filename : ")
inp1 = input("Enter privatekey filename : ")
with open(inp1) as df:
    data = df.read()
    pv = data.strip().split("\n")
#inp2 = "publickey1.txt"
with open(inp2) as df:
    data = df.read()
    pb = data.strip().split("\n")
simmer = list(zip(pv,pb))
for i in simmer:
    if i[0][0].isnumeric():
        for j in range(len(i[0])):
            print(atoz[(ord(i[0][j]) + ord(i[1][j]))%26],end="")
    else:
        for j in range(len(i[0])):
            print(AtoZ[(ord(i[0][j]) + ord(i[1][j]))%26],end="")
    print()