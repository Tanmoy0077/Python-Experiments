def flip_bits(arr, n):
    '''
    arr : an array
    n : size of the array
    '''
    prev1 , count0, next1, maxcount0= 0, 0, 0, 0
    for i in range(n):
        if arr[i] == 1:
            prev1 += 1
        else:
            for j in range(i, n):
                if arr[j] == 0:
                    count0 += 1
                else:
                    next1 += 1
                    if next1>=count0:
                        count0 = 0
                        prev1 += next1
                        next1 = 0
                maxcount0 = max(maxcount0, count0)
            break
    return prev1+maxcount0

arr = [1,0,0,1,1,1,0]
print(flip_bits(arr, len(arr)))
# 1,0,0,1,0
# 1,0,0,1,1,0
# 1,0,0,1,1,1,0
# 1,0,0,1,1,0,1,0