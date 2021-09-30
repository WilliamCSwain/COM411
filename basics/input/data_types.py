print("Please input your name.")
name = input()
print("Please enter your age.")
age = int(input())
print("Please enter your weight.")
weight = float(input())
print("Please enter your height.")
height = float(input())

bmi = weight / (height ** 2)

print(f"{name} your bmi is: {bmi}")