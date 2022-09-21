n = int(input("Enter the number of lines : "))
i = 1
while i<=n:
    j = n - i
    while j >= 1:
        print(" ", end="")
        j = j - 1
    j = i
    while j >= 1:
        print(j, end="")
        j = j - 1
    j = 2
    while j <= i:
        print(j, end="")
        j = j + 1
    print()
    i = i + 1
