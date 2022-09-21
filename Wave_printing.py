def wavePrint(mat, nRows, mCols):
    """This will print the matrix in the format of sine wave"""
    for j in range(mCols):
        if j%2==0:
            for i in range(nRows):
                print(mat[i][j], end=" ")
        else:
            for i in range(nRows-1, -1, -1):
                print(mat[i][j], end=" ")

li = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
wavePrint(li, 3, 4)