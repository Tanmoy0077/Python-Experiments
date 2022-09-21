def sumOfTwoArrays(arr1, n, arr2, m, output): 
    carry = 0
    i = n - 1
    j = m - 1
    k = max(m,n)
    while i>=0 and j>=0:
        temp = arr1[i] + arr2[j] + carry
        if temp > 9:
            carry = temp // 10
            temp = temp % 10
        else:
            carry = 0
        output[k]=temp
        k -= 1
        i -= 1
        j -= 1
    while i >= 0:
        temp = arr1[i] + carry
        if temp > 9:
            carry = temp // 10
            temp = temp % 10
        else:
            carry = 0
        output[k]=temp
        k -= 1
        i -= 1
    while j >= 0:
        temp = arr2[j] + carry
        if temp > 9:
            carry = temp // 10
            temp = temp % 10
        else:
            carry = 0
        output[k]=temp
        k -= 1
        j -= 1
    while k >= 0:
        if carry != 0:
            temp = carry
            carry = 0
        else:
            temp = 0
        output[k]=temp
        k -= 1

arr1 = [6,9,8,5]
arr2 = []
output = [0,0,0,0,0]
sumOfTwoArrays(arr1, len(arr1), arr2, 0, output)
print(output)