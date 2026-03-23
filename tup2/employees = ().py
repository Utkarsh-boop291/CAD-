employees = ()

while True:
    print("1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        emp_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        salary = int(input("Enter Salary: "))
        employees = employees + ((emp_id, name, salary),)

    elif ch == 2:
        for e in employees:
            print(e)

    elif ch == 3:
        emp_id = int(input("Enter ID to search: "))
        found = False
        for e in employees:
            if e[0] == emp_id:
                print(e)
                found = True
        if not found:
            print("Not Found")

    elif ch == 4:
        emp_id = int(input("Enter ID to update: "))
        temp = []
        for e in employees:
            if e[0] == emp_id:
                name = input("Enter New Name: ")
                salary = int(input("Enter New Salary: "))
                temp.append((emp_id, name, salary))
            else:
                temp.append(e)
        employees = tuple(temp)

    elif ch == 5:
        emp_id = int(input("Enter ID to delete: "))
        temp = []
        for e in employees:
            if e[0] != emp_id:
                temp.append(e)
        employees = tuple(temp)

    elif ch == 6:
        break