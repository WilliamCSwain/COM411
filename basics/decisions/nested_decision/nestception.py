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