def isVowel(string):
    """ This function checks if a character is a vowel or consonant """
    vowel = ['A', 'E', 'I', 'O', 'U']
    if string in vowel:
        return True
    else:
        return False


s = input("Enter the word in capital letters : ")
l1, l2 = {}, {}
c, v = 0, 0
# # Finding the index form the vowel and consonant starts
# for i in range(len(s)):
#     if isVowel(s[i]):
#         v = i
#         for j in range(i + 1, len(s)):
#             if not isVowel(s[j]):
#                 c = j
#                 break
#         break
#     else:
#         c = i
#         for j in range(i + 1, len(s)):
#             if isVowel(s[j]):
#                 v = j
#                 break
#         break
# print(v, c)
# for i in range(len(s)):
#     if(isVowel(s[i])):
#         for j in range(len(s[i:])):
#             if s[i:i + j + 1] not in l2.keys():
#                 l2[s[i:i + j + 1]] = 1
#             else:
#                 l2[s[i:i + j + 1]] += 1
#     else:
#         for j in range(len(s[i:])):
#             if s[i:i + j + 1] not in l1.keys():
#                 l1[s[i:i + j + 1]] = 1
#             else:
#                 l1[s[i:i + j + 1]] += 1
for i in range(len(s)):
    if isVowel(s[i]):
        v += len(s[i:])
    else:
        c += len(s[i:])

print(c,v)
# print(l1)
# print(l2)
# Storing all the possible combinations of words starts with consonants
# if c is not None:
#     for i in range(c, len(s)):
#         if not isVowel(s[i]):
#             for j in range(len(s[i:])):
#                 if s[i:i + j + 1] not in l1.keys():
#                     l1[s[i:i + j + 1]] = 1
#                 else:
#                     l1[s[i:i + j + 1]] += 1
# # Storing all the possible combinations of words starts with vowels
# if v is not None:
#     for i in range(v, len(s)):
#         if isVowel(s[i]):
#             for j in range(len(s[i:])):
#                 if s[i:i + j + 1] not in l2.keys():
#                     l2[s[i:i + j + 1]] = 1
#                 else:
#                     l2[s[i:i + j + 1]] += 1

# print(l1, '\n', l2)
# stuart, kevin = 0, 0
# if l2:
#     kevin = sum([i for i in l2.values()])
# if l1:
#     stuart = sum([i for i in l1.values()])
# print("The sum of the 1st list is : ", stuart)
# print("The sum of the 2nd list is : ", kevin)
stuart = c
kevin = v
if stuart > kevin:
    print("1st player wins the game : Score :", stuart)
elif stuart < kevin:
    print("2nd player wins the game : Score :", kevin)
else:
    print("Match tied : Score : ", stuart)
