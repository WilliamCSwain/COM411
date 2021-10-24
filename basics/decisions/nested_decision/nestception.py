print("Where should I look?") # Asks for the place
place = input()

if place == "in the bedroom":
    print("Where in the bedroom should I take a look?")
    bedroom_place = input()

    if bedroom_place == "under the bed":
        print("Found shoes, no battery.")
    else:
        print("Found mess, no battery.")
