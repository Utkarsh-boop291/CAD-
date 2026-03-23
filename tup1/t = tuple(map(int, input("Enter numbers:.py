t = tuple(map(int, input("Enter numbers: ").split()))

lst = list(t)
lst.sort()
t = tuple(lst)

print(t)

key = int(input("Search: "))
if key in t:
    print("Found at index", t.index(key))
else:
    print("Not found")