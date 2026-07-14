n=int(input("Enter n:")) 
for row in range(1,n+1):
    for count in range (1,n-row+1):
        print(" ",end="")
    for count in range(1,row+1):
        print(count,end="")
    for count in range(row-1,0,-1):
        print(count,end="")
    print()

for row in range(n-1,0,-1):
    for count in range(1,n-row+1):
        print(" ", end="")
    for count in range(1,row+1):
        print(count, end="")
    for count in range(row-1,0,-1):
        print(count,end="")
    print()

    