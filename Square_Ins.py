n = int(input("Enter the number of lines : "))
k = 1
count = 0
for i in range(1, n+1,2):
    for j in range(0, n):
        print(k+j, end=" ")
    k = ((i+1)*n)+1
    count = count + 1
    print()
rem = n - count
if n % 2 == 0:
    k = (n * (n-1))+1
    for i in range(1, rem+1):
        for j in range(0, n):
            print(k+j, end=" ")
        k = k - (2*n)
        print()
else:
    k = n * n
    for i in range(1, rem+1):
        k = (k - (2*n))+1
        for j in range(0, n):
            print(k+j, end=" ")
        k = k -1
        print()
