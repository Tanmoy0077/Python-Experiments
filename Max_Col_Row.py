def max_col_row(li, col, row):
    max_col = -245
    max_row = -245
    for j in range(col):
        s = 0
        for ele in li:
            s += ele[j]
        if(s > max_col):
            max_col = s
            max_col_i = j
    for i in range(row):
        s = 0
        for ele in li[i]:
            s += ele
        if (s > max_row):
            max_row = s
            max_row_i = i
    if(max_row >= max_col):
        print("row "+str(max_row_i)+" "+str(max_row))
    else:
        print("column "+str(max_col_i)+" "+str(max_col))

li = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
max_col_row(li, 4, 4)