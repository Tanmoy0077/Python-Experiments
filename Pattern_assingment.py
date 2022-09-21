n = int(input("Enter the number of lines : "))
i = 1
while i<=n:
    j = 1
    while j<=i:
        if(j == i):
            print("*", end="")
        else:
            print("0", end="")
        j = j + 1
    j = 1
    while j <= (n-i+1):
        if(j == (n-i+1)):
            print("*", end="")
        else:
            print("0", end="")
        j = j + 1
    j = 1
    while j <= (n-i+1):
        if(j == (n-i+1)):
            print("*", end="")
        else:
            print("0", end="")
        j = j + 1
    j = 1
    while j <= i-1:
        print("0", end="")
        j = j + 1
    print()
    i = i + 1