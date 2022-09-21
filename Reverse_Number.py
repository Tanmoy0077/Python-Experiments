# My Method

num = input("Enter the number : ")
num2 = num[::-1]
if (num2[-1]=="-"):
    print(int(num2[:-1])*(-1))
else:
    print(int(num2))

# Traditional Method

# num = int(input("Enter the Number : "))
# temp = abs(num)
# rev = 0
# while temp > 0:
#     rem = temp % 10
#     rev = (rev * 10) + rem
#     temp = temp // 10
# if num<0:
#     print("Reverse of the Number is :", rev*(-1))
# else:
#     print("Reverse of the Number is :", rev)