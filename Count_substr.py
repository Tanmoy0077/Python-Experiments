def count_substring(string, sub_string):
    sublen = len(sub_string)
    count = 0
    for i in range(len(string)-sublen+1):
        temp = string[i:i+sublen]
        if temp == sub_string:
            count += 1
    return count

print(count_substring("ABCDCDCD", "CD"))