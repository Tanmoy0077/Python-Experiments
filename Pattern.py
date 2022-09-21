"""
n = int(input("Enter the number of rows : "))
i = 1
while i <= n:
    j = 1
    k = ord('A') + (n-i)
    while j<=i:
        print(chr(k+j-1), end='')
        j = j+1
    print()
    i = i + 1
"""
"""
n =int(input("Enter the number of rows : "))
i = 1
while i<=n:
    j = 1
    if i == 1:
        print(1, end='')
    if i >1:
        while j<=i:
            if j==1 or j==i:
                print(i-1, end='')
            else:
                print(0, end='')
            j = j+1
    print()
    i = i+1
"""
"""
n = int(input("Enter the number of rows : "))
i = 1
while i<=n:
    spaces = 1
    while spaces <= n - i:
        print(" ", end="")
        spaces = spaces + 1
    star = 1
    while star <= i:
        print(star, end='')
        star = star + 1
    star = i -1
    while star >= 1:
        print(star, end='')
        star = star - 1
    print()
    i = i + 1
"""

num = int(input())
i = 1
n1 = (num // 2) + 1
n2 = n1 - 1
while i<=n1:
    spaces = 1
    while spaces <= n1 - i:
        print(" ", end="")
        spaces = spaces + 1
    star = 1
    while star <= (2*i)-1:
        print("*", end='')
        star = star + 1
    print()
    i = i + 1
i = n2
while i >= 1:
    spaces = 1
    while spaces <= n1 - i:
        print(" ", end="")
        spaces = spaces + 1
    star = 1
    while star <= (2*i)-1:
        print("*", end='')
        star = star + 1
    print()
    i = i - 1

"""
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    j = 1
    while j <= n - i:
        print(" ", end="")
        j = j + 1
    j = 1
    while j <= i:
        print(i-j+1, end="")
        j = j + 1
    print()
    i = i + 1
"""
