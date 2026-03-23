queue = []

while True:
    print("1.Book Ticket 2.Serve Ticket 3.View Queue 4.Search 5.Count 6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Enter name: ")
        queue.append(name)

    elif ch == 2:
        if queue:
            print("Served:", queue.pop(0))
        else:
            print("No customers")

    elif ch == 3:
        for i in range(len(queue)):
            print(i+1, queue[i])

    elif ch == 4:
        name = input("Enter name to search: ")
        if name in queue:
            print("Position:", queue.index(name) + 1)
        else:
            print("Not found")

    elif ch == 5:
        print("Total customers:", len(queue))

    elif ch == 6:
        break