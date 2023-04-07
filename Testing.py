# li1 = set(int(i) for i in input("Enter the values of the 1st list : ").split())
# li2 = set(int(i) for i in input("Enter the values of the 2nd list : ").split())
# print("First is subset of second set - ",li1.issubset(li2))
# print("Second is subset of first set - ",li2.issubset(li1))
# print("First is super set of second set - ",li1.issuperset(li2))
# print("Second is super set of first set - ",li2.issuperset(li1))

# if (li1.issubset(li2)) or (li1.issuperset(li2)):
#     li1 = set()
# elif (li2.issubset(li1)) or (li1.issuperset(li2)):
#     li2 = set()
# print("First set : ",li1)
# print("Second set : ",li2)


li = [int(i) for i in input("Enter the values of the list : ").split()]
li = [li[-1]] + li[:len(li) - 1]
print("The list after rotating is : ",li)