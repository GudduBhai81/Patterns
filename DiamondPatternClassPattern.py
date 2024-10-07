rowSize = int(input("Enter the numere of rows = "))
if rowSize%2==0:
    halfDiaRow = int(rowSize/2)
else:
    halfDiaRow = int(rowSize/2)
space = halfDiaRow-1
for i in range(1, halfDiaRow+1):
    for j in range(1, space+1):
        print(end=" ")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        number = num+1
    print()
space = 1
for i in range(1, halfDiaRow):
    for j in range(1, space+1):
        print(end=" ")
    space = space+1
    num = 1
    for j in range(1, 2*(halfDiaRow-i)):
        print(end=str(num))
        number = num+1
    print()