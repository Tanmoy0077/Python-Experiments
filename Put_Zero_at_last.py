def pushZerosAtEnd(arr, n):
    for i in range(n):
        if arr[i] == 0:
            for j in range(i+1, n):
                if arr[j] != 0:
                    (arr[i], arr[j]) = (arr[j], arr[i])
                    i += 1
            break
ln = [7,0,0,0,0,0,5,0,7,4,8,0,0,1,3,0,7,2,0]
pushZerosAtEnd(ln,len(ln))
print(ln)
