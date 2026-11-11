#Name: Isis Autry
# Text-Based Adventure Game: Meleena's Escape
# Based directly on pseudocode from Fantasy_Game_Pseudocode.docx

# ---------------------------------------------------------
# Function: Show game instructions
# ---------------------------------------------------------
def show_instructions():
    print("====================================")
    print("        MELEENA'S ESCAPE GAME")
    print("====================================")
    print("You awaken in a dark room after being kidnapped by Gisella.")
    print("Collect all 7 spell ingredients before entering the Bedroom.")
    print("Only then can you cast the sleeping spell and escape.")
    print("------------------------------------")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("====================================\n")


# ---------------------------------------------------------
# Function: Show player status
# ---------------------------------------------------------
def show_status(current_room, inventory, rooms):
    print("\n------------------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)

    # Show item in the room (if any)
    if "contains" in rooms[current_room] and rooms[current_room]["contains"] != "None":
        print("You see a", rooms[current_room]["contains"])
    print("------------------------------")


# ---------------------------------------------------------
# Main game function
# ---------------------------------------------------------
def main():

    # -----------------------------------------------------
    # Dictionary linking rooms + items (EXACT from pseudocode)
    # -----------------------------------------------------
    rooms = {
        "Empty Room": {
            "north": None,
            "south": None,
            "east": "Library",
            "west": None,
            "contains": "None"
        },
        "Library": {
            "north": "Potions Room",
            "south": "Waterfall",
            "east": "Kitchen",
            "west": "Empty Room",
            "contains": "Book"
        },
        "Potions Room": {
            "north": None,
            "south": "Library",
            "east": "Greenhouse",
            "west": None,
            "contains": "Vial"
        },
        "Greenhouse": {
            "north": None,
            "south": "Kitchen",
            "east": None,
            "west": "Potions Room",
            "contains": "Lotus Flower"
        },
        "Kitchen": {
            "north": "Greenhouse",
            "south": "Dungeon",
            "east": "Bedroom",
            "west": "Library",
            "contains": "Ladle"
        },
        "Bedroom": {
            "north": None,
            "south": "Garden",
            "east": None,
            "west": "Kitchen",
            "contains": "Gisella"  # Villain
        },
        "Garden": {
            "north": "Bedroom",
            "south": None,
            "east": None,
            "west": "Dungeon",
            "contains": "Lavender"
        },
        "Dungeon": {
            "north": "Kitchen",
            "south": "Waterfall",
            "east": "Garden",
            "west": None,
            "contains": "Cauldron"
        },
        "Waterfall": {
            "north": "Library",
            "south": None,
            "east": "Dungeon",
            "west": None,
            "contains": "Spring Water"
        }
    }

    # Starting conditions
    current_room = "Empty Room"
    inventory = []
    required_items = 7  # Book, Vial, Lotus Flower, Ladle, Lavender, Spring Water, Cauldron

    show_instructions()

    # -----------------------------------------------------
    # Gameplay loop
    # -----------------------------------------------------
    while True:
        show_status(current_room, inventory, rooms)

        # Get player input
        command = input("Enter your move: ").lower().strip()

        # -------------------------------------------------
        # Handle movement commands
        # -------------------------------------------------
        if command.startswith("go "):
            direction = command[3:]  # Extract direction

            if direction in rooms[current_room] and rooms[current_room][direction] is not None:
                current_room = rooms[current_room][direction]
            else:
                print("You cannot go that way.")

        # -------------------------------------------------
        # Handle item collection
        # -------------------------------------------------
        elif command.startswith("get "):
            item_name = command[4:]

            if rooms[current_room]["contains"] == item_name:
                inventory.append(item_name)
                print(item_name, "added to inventory.")
                rooms[current_room]["contains"] = "None"
            else:
                print("You can't get that item.")

        # -------------------------------------------------
        # Invalid command
        # -------------------------------------------------
        else:
            print("Invalid command. Try again.")

        # -------------------------------------------------
        # Lose condition: Enter Bedroom before collecting all items
        # -------------------------------------------------
        if current_room == "Bedroom":
            if len(inventory) == required_items:
                print("\nYou confront Gisella with the completed spell!")
                print("She collapses into a deep sleep. You escape the castle!")
                print("Congratulations — you won!")
            else:
                print("\nGisella appears before you!")
                print("You are unprepared... Meleena is captured.")
                print("GAME OVER.")
            print("Thanks for playing!")
            break

        # -------------------------------------------------
        # Win condition: All items collected (player must still reach Bedroom)
        # -------------------------------------------------
        if len(inventory) == required_items:
            print("\nYou have collected all 7 ingredients!")
            print("Find Gisella in the Bedroom to cast the spell!")


# Run the game
if __name__ == "__main__":
    main()