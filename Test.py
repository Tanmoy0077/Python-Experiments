# import math
# def sumofsquares(n):
#       for i in range(math.floor(math.sqrt(n))+1):
#         for j in range(math.floor(math.sqrt(n))+1):
#           if (i*i + j*j) == n:
#             return True
#       return (False)    
      
  

# print(sumofsquares(10))
# str1 = "h"
# l1 = []
# pattern = input()
# while str1 != "":
#   str1 = input()
#   if pattern in str1:
#     l1.append(str1)
# for i in l1:
#   print(i)

# def maxaggregate(l):
#   d = {}
#   em = []
#   for i in l:
#     if i[0] not in d.keys():
#       d[i[0]] = i[1]
#     else:
#       d[i[0]] += i[1]
#   maxsc = max(d.values())
#   for i in d.keys():
#         if d[i] == maxsc:
#               em.append(i)
#   return (sorted(em))

# print(maxaggregate([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',22),('Ashwin',47)]))

def recur(l1,l2):
  alo = 0
  em = []
  for i in range(len(l1)):
    for j in range(alo, len(l2)):
      if l1[i] == l2[j]:
        alo = j+1
        em.append(l1[i])
        break
    