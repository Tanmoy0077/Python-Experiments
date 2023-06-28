def equilibrium(a, n):
    if n == 1:
        return 0
    if n == 2:
        return -1
    lsum = a[0]
    rsum = sum(a[1:])
    for p in range(1, n-1):
        if lsum == rsum - a[p]:
            return p
        lsum += a[p]
        rsum -= a[p]
    return -1


li = [1,3,2,4,0]
print(equilibrium(li, len(li)))