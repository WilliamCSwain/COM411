print("Calculating the sum of the first 100 numbers.")
number_to_sum = int(input())

summed = 0

print()
total = 0
while summed < number_to_sum:
    print(f"Please enter number {summed} of {number_to_sum}:")
    number = int(input())
    total = total + number
    summed = summed + 1

print(f"The answer is {total}.")