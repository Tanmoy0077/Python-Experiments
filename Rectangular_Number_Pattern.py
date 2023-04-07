n = int(input("Enter the number of lines : "))
for i in range(1, n+1):
    for j in range(1, i):
        print(n-j+1, end=" ")
    for j in range(1, (2*n)-((2*i)-1)+1):
        print(n-i+1, end=" ")
    for j in range(1, i):
        print(n-i+j+1, end=" ")
    print()
for i in range(n-1, 0,-1):
    for j in range(1, i):
        print(n-j+1, end=" ")
    for j in range(1, (2*n)-((2*i)-1)+1):
        print(n-i+1, end=" ")
    for j in range(1, i):
        print(n-i+j+1, end=" ")
    print()