def spiralPrint(mat, nRows, mCols):
    """This will print the matrix in spiral order"""
    i = 0
    j = 0
    count = 0
    while True:
        while j<mCols:
            print(mat[i][j],end=" ")
            mat[i][j] = -245
            j += 1
        j -= 1
        i += 1
        while i<nRows:
            print(mat[i][j],end=" ")
            mat[i][j] = -245
            i += 1
        i -= 1
        j -= 1
        while j>=count:
            print(mat[i][j],end=" ")
            mat[i][j] = -245
            j -= 1
        j += 1
        i -= 1
        while i > count:
            print(mat[i][j],end=" ")
            mat[i][j] = -245
            i -= 1
        i += 1
        j += 1
        mCols -= 1
        nRows -= 1
        count += 1
        if mat[i][j] == -245:
            break

li = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
spiralPrint(li,5,5)
# print(li)