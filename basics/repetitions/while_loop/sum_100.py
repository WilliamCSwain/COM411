print("Calculating the sum of the first 100 numbers...")

number = 1
total = 0

while number <= 100:
    total = total + number
    number = number + 2

    print(f"...Done! The answer is {total}!")