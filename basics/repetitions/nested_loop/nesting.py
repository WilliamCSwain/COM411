print("How many rows should there be?")
rows = int(input())

print("How many columns should there be?")
columns = int(input())

for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(":-)", end="")
    print()