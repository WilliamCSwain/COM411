print("What phrase do you see?")
phrase = input()

print("\nReversing...")
print("The phrase is ", end="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed)