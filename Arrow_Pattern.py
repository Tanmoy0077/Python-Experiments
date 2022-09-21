n = int(input("Enter the number of lines : "))
n1 = (n//2)+1
n2 = n - n1
i = 1
while i <= n1:
    spaces = 1
    while spaces <= i - 1:
        print(" ", end="")
        spaces =spaces + 1
    star = 1
    while star <= i:
        print("* ", end="")
        star = star + 1
    print()
    i = i + 1
i = n2
while i >= 1:
    spaces = 1
    while spaces <= i - 1:
        print(" ", end="")
        spaces =spaces + 1
    star = 1
    while star <= i:
        print("* ", end="")
        star = star + 1
    print()
    i = i - 1