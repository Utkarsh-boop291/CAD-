students = ()

while True:
    print("1.Add 2.View 3.Topper 4.Search 5.Sort 6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        roll = int(input("Enter roll: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students = students + ((roll, name, marks),)

    elif ch == 2:
        for s in students:
            print(s)

    elif ch == 3:
        if students:
            top = students[0]
            for s in students:
                if s[2] > top[2]:
                    top = s
            print(top)

    elif ch == 4:
        roll = int(input("Enter roll to search: "))
        found = False
        for s in students:
            if s[0] == roll:
                print(s)
                found = True
        if not found:
            print("Not found")

    elif ch == 5:
        temp = list(students)
        temp.sort(key=lambda x: x[2], reverse=True)
        students = tuple(temp)
        print(students)

    elif ch == 6:
        break