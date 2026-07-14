# 1
# 12
# 123
# 1234
# 12345

# rows 1 to N
# count 1 to N

n=int(input("Enter n"))
for row in range(1,n+1):
    for count in range(1, row+1):
        print(count,end="")
    print() 



