"""LeetCode Problem : 80 ms Runtime"""

def clearlist(li: list, index: int):
    for i in range(index+1):
        li.pop(0)


def noRepeat(string: str):
    lst = []
    maximum = 0
    if(len(string)==0):
        return 0
    for i in range(len(string)):
        temp = string[i]
        if(temp not in lst):
            lst.append(temp)
        else:
            li = len(lst)
            if(li>maximum):
                maximum = li
            if(string[i-1]==temp):
                lst.clear()
            else:
                clearlist(lst, lst.index(temp))
            lst.append(temp)
    li = len(lst)
    if(li>maximum):
        return(li)
    return maximum

print(noRepeat("abcabcbb"))