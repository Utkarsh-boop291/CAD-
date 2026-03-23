books = {}

while True:
    print("1.Add 2.Issue 3.Return 4.View 5.Exit")
    ch = int(input())

    if ch == 1:
        b = input("Book: ")
        books[b] = "Available"

    elif ch == 2:
        b = input("Book: ")
        if b in books and books[b] == "Available":
            books[b] = "Issued"

    elif ch == 3:
        b = input("Book: ")
        if b in books:
            books[b] = "Available"

    elif ch == 4:
        for b in books:
            print(b, books[b])

    elif ch == 5:
        break