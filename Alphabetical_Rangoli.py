n = int(input("Enter the number of lines : "))
for i in range(n//2+1):
    m = 97+(n//2)
    for j in range(n//2, i, -1):
        print("--", end="")
    for j in range(i+1):
        if i != 0:
            print(chr(m), end="-")
            m -= 1
        else:
            print(chr(m), end="")
            m -= 1
    m += 2
    for j in range(i):
        print(chr(m), end="")
        m += 1
        if j != i-1:
            print("-", end="")
    for j in range(n//2, i, -1):
        print("--", end="")
    print()
for i in range(n//2):
    m = 97 + (n//2)
    for j in range(i+1):
        print("--", end="")
    for j in range(n//2, i, -1):
        print(chr(m), end="-")
        m -= 1
    m += 2
    for j in range(n//2-1,i,-1):
        print(chr(m), end="-")
        m += 1
    for j in range(2*i+1):
        print("-", end="")
    print()
    