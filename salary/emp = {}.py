emp = {}

while True:
    print("1.Add 2.View 3.Highest 4.Search 5.Exit")
    ch = int(input())

    if ch == 1:
        id = int(input())
        name = input()
        sal = int(input())
        emp[id] = {"name": name, "sal": sal}

    elif ch == 2:
        for i in emp:
            print(i, emp[i])

    elif ch == 3:
        if emp:
            m = max(emp, key=lambda x: emp[x]["sal"])
            print(m, emp[m])

    elif ch == 4:
        id = int(input())
        if id in emp:
            print(emp[id])

    elif ch == 5:
        break