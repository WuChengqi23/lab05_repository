print("Hello World")
print("Hello World")
print("Hello World")

while True:
    try:
        age = int(input("What's your age?\n"))
        if age < 0 or age > 100:
            print("fuck")
            continue
        break
    except ValueError:
        print("SB")
print(f"Your age is {age}")
