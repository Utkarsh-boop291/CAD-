students = {
    1: {"name": "Aman", "marks": 85},
    2: {"name": "Ravi", "marks": 90}
}

for key, value in students.items():
    print(key, value["name"], value["marks"])