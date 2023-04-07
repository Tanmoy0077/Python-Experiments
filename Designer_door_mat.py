n = int(input("Enter the number of lines : "))
m = 3*n
for i in range((n//2)):
    for j in range((n//2)*3-i*3):
        print('-', end="")
    for j in range(2*i+1):
        print(".|.", end="")
    for j in range((n//2)*3-i*3):
        print('-', end="")
    print()
print("WELCOME".center(m, '-'))
for i in range((n//2)-1, -1, -1):
    for j in range((n//2)*3-i*3):
        print('-', end="")
    for j in range(2*i+1):
        print(".|.", end="")
    for j in range((n//2)*3-i*3):
        print('-', end="")
    print()