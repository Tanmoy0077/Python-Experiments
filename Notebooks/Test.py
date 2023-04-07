dq = []


def inpleft(l):
    val = int(input("Enter the value : "))
    l.insert(0, val)
    print(val, "is inserted at begining")


def inpright(l):
    val = int(input("Enter the value : "))
    l.append(val)
    print(val, "is inserted at last")


def delleft(l):
    print(f"{l.pop()} is Popped from the Deque")


def delright(l):
    print(f"{l.pop(0)} is Popped from the Deque")


def rev(l):
    global dq
    dq = dq[::-1]
    print("Deque is reversed")


def display(l):
    print("The Deque is : ", l)


print("1. Insert Left")
print("2. Insert Right")
print("3. Reverse")
print("4. Delete Left")
print("5. Delete Right")
print("6. Display")
print("7. Exit")
options = {1: inpleft, 2: inpright, 3: rev, 4: delleft, 5: delright, 6: display}
while (True):
    choice = int(input("Enter your choice : "))
    if choice in options.keys():
        options[choice](dq)
    elif choice == 7:
        print("Exiting")
        break
    else:
        print("Invalid Input")
