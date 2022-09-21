def short_path(time, start, stop):
    """ Leet Code Problem """
    unique = []
    table =[]
    # Creating a list of unique elements from the 'time' list 
    for i in range(len(time)):
        if(time[i][0] not in unique):
            unique.append(time[i][0])
        if(time[i][1] not in unique):
            unique.append(time[i][1])
    unique.sort()
    # Creating a table of required time to move form one node to another node
    for i in range(len(unique)):
        table.append([-1]*len(unique))
    for i in time:
        row = i[0]-1
        col = i[1]-1
        if(table[row][col] == -1):
            table[row][col] = i[2]
            table[col][row] = i[2]
    print(table)
    


li = [[1, 2, 1], [2, 3, 1], [3, 4, 1]]
short_path(li, 0, 0)
