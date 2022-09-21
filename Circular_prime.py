num = input("Enter the number : ")
flag = False
for i in range(len(num)):
    temp = int(num)
    for j in range(2, int(temp**0.5)):
        if temp % j == 0:
            flag = True
            break
    if flag == True:
        print("This is not a circular prime number")
        break
    num = num[1:] + num[0]
else:
    print("This is a circular prime number")