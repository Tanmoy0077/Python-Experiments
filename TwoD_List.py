temp = input("Enter the number of rows and columns : ").split()
n, m = int(temp[0]), int(temp[1])
"""
print("Enter the values :")
# Each row should be given as space seperated input and press enter before giving the second row
li = [[int(i) for i in input().split()] for j in range(n)]
"""
# Each row should be given as space seperated input
temp = input("Enter the values : ").split()
li = [[int(temp[m*i+j]) for j in range(m)] for i in range(n)]
print("The 2-D List is : ")
for ele in li:
    out = " ".join([str(x) for x in ele])
    print(out)