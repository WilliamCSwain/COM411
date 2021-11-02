print("Which brightness level is required?")
brightness_desired = int(input())

print("\nAdjusting the brightness..\n")

for brightness in range(2, brightness_desired + 1, 2):
    print(f"Beep's brightness level: {'*' * brightness}")
    print(f"Bop's brightness level: {'*' * brightness}")

print("Adjustments have been completed.")