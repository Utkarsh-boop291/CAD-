accounts = {}

while True:
    print("1.Create 2.Deposit 3.Withdraw 4.Check 5.All 6.Exit")
    ch = int(input())

    if ch == 1:
        acc = int(input("Acc No: "))
        name = input("Name: ")
        bal = int(input("Balance: "))
        accounts[acc] = {"name": name, "bal": bal}

    elif ch == 2:
        acc = int(input("Acc No: "))
        if acc in accounts:
            amt = int(input("Amount: "))
            accounts[acc]["bal"] += amt

    elif ch == 3:
        acc = int(input("Acc No: "))
        if acc in accounts:
            amt = int(input("Amount: "))
            if accounts[acc]["bal"] >= amt:
                accounts[acc]["bal"] -= amt

    elif ch == 4:
        acc = int(input("Acc No: "))
        if acc in accounts:
            print(accounts[acc])

    elif ch == 5:
        for a in accounts:
            print(a, accounts[a])

    elif ch == 6:
        break