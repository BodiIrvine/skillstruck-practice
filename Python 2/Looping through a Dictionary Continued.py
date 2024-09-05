ride = {
    "Alice": 110,
    "Bob": 95,
    "Charlie": 105,
    "David": 99,
    "Eve": 120
}

for x in ride.values():
    if x >= 100:
        print("This person is tall enough to ride")
    else:
        print("This person is too short to ride")
