nums = list(map(int, input().split()))

while True:
    print("1.Even 2.Odd 3.Max 4.Min 5.Sum 6.Exit")
    ch = int(input())

    if ch == 1:
        print([x for x in nums if x % 2 == 0])

    elif ch == 2:
        print([x for x in nums if x % 2 != 0])

    elif ch == 3:
        print(max(nums))

    elif ch == 4:
        print(min(nums))

    elif ch == 5:
        print(sum(nums))

    elif ch == 6:
        break