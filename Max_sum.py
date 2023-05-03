def maxSubSumKConcat(arr, n, k):
    ans = 0
    maxsum = float('-inf')
    start = 0
    end = n-1
    for i in range(n):
        ans += arr[i]
        if maxsum < ans:
            maxsum = ans
            end = i
        if ans<0:
            start=i
            ans=0
    if (start == 0) and (end == n-1):
        return maxsum*k
    

