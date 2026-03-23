while True:
    print("1.Add 2.Sub 3.Mul 4.Div 5.Exit")
    ch = int(input())

    if ch == 5:
        break

    a = int(input())
    b = int(input())

    if ch == 1:
        print(a + b)
    elif ch == 2:
        print(a - b)
    elif ch == 3:
        print(a * b)
    elif ch == 4:
        if b != 0:
            print(a / b)