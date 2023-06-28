from collections import OrderedDict

d = OrderedDict()
n = int(input("Enter the number of items : "))
print("Enter the items and their prices : ")
for i in range(n):
    temp = input().split()
    if temp[0] in d.keys():
        d[temp[0]] += int(temp[1])
    else:
        d[temp[0]] = int(temp[1])

print("The items are : ", d)