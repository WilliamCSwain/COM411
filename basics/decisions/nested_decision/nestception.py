print("Where should I look?") # Asks for the place
place = input()

# Bedroom Checks
if place == "in the bedroom":
    print("Where in the bedroom should I take a look?")
    bedroom_place = input()

    if bedroom_place == "under the bed":
        print("Found shoes, no battery.")
    else:
        print("Found mess, no battery.")

# Bathroom Checks
elif place == "in the bathroom":
    print("Where in the bathroom should I check?")
    bathroom_place = input()

    if bathroom_place == "in the bathtub":
        print("Found rubber duck, no battery.")
    else:
        print("Found wet surface, no battery.")

# Lab Checks
elif place == "in the lab":
    print("Where in the lab should I look?")
    lab_place = input()

    if lab_place == "on the table":
        print("Yes! Battery has been found.")
    else:
        print("Tools found, no battery.")

# Unknown Place Check
else:
    print("Location unsure. Please try another location.")