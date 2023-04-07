n = int(input("Enter the number of students : "))
record = []
gradeList = []
for i in range(n):
    name = input(f"Enter the name of the student {i+1} : ")
    grade = float(input(f"Enter the grade of the student {i+1} : "))
    gradeList.append(grade)
    record.append([name, grade])
sets = {item for item in gradeList}
gradeList = list(sets)
gradeList.sort()
nameList = [i[0] for i in record if i[1] == gradeList[1]]
nameList.sort()
print("Students who get the second lowest grade are : ")
for item in nameList:
    print(item)