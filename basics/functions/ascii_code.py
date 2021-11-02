print("Program Started.")

print("Please enter a standard character:")
character = input()

if len(character) == 1:
    print(f"The ASCII code for {character} is {ord(character)}")
else:
    print("A singular character was expected.")

print("The program is now ended.")