print("What phrase do you see?")
phrase = input()

print("\nReversing...")
print("The phrase is ", end="")

for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")