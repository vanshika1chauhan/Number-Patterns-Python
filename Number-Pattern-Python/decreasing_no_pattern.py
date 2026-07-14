# rows N to 1
# spaces 1 to n-row, counting 1 to rows

n=int(input("Enter n="))

for row in range (n,0,-1):
      
    for count in range(1, row+1):
        print(count,end="")
    for count in range(row-1,0,-1):
        print(count,end='')
    print() 




