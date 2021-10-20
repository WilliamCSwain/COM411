print("Which direction should I paint? (Select up, down, left or right)")
direction = input()

if direction == "up":
    print("I am painting in an upward direction.")
elif direction == "down":
    print("I am painting in a downward direction.")
elif direction == "right":
    print("I am painting in a rightward direction.")
elif direction == "left":
    print("I am painting in a leftward direction.")
else:
    print("Unfortunately I'm not sure which direction I am painting in.")