age = int(input("Age: "))
day = input("Day: ").strip()

if age < 5:
    print("Free entry!")
else:
    if age <= 12:
        price = 50000
    elif age >= 60:
        price = 60000
    else:
        price = 100000

    if day == "سه‌شنبه":
        price *= 0.8

    print(f"Ticket price: {price:.0f} toman")
