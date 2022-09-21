num = int(input("Enter the number of lines : "))
for i in range(1, num+1):
    for j in range(1, i):
        print(" ", end="")
    for j in range(i, num+1):
        print(j, end="")
    print()
for i in range(1, num):
    for j in range(1, num-i):
        print(" ", end="")
    for j in range(num-i, num+1):
        print(j, end="")
    print()
