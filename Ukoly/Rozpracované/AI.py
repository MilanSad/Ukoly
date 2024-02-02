players = {}  # Dictionary to store player information

def add_player():
    full_name = input("Enter player's full name: ")
    height = float(input("Enter player's height (cm): "))
    players[full_name] = height

def delete_player():
    full_name = input("Enter the full name of the player to delete: ")
    if full_name in players:
        del players[full_name]
        print(f"Player {full_name} deleted successfully.")
    else:
        print("Player not found.")


def search_player():
    full_name = input("Enter the full name of the player to search: ")
    if full_name in players:
        height = players[full_name]
        print(f"Player: {full_name}, Height: {height} cm")
    else:
        print("Player not found.")

def replace_player():
    old_name = input("Enter the full name of the player to replace: ")
    if old_name in players:
        new_name = input("Enter the new full name: ")
        new_height = float(input("Enter the new height (cm): "))
        players[new_name] = new_height
        del players[old_name]
        print(f"Player {old_name} replaced with {new_name} successfully.")
    else:
        print("Player not found.")

def show_all_players():
    if not players:
        print("No players added yet.")
        return

    print("List of players:")
    for name, height in players.items():
        print(f"- {name} ({height} cm)")
    print(players)

while True:
    print("\nBasketball Player App:")
    print("1. Add player")
    print("2. Delete player")
    print("3. Search player")
    print("4. Replace player")
    print("5. Show all players")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_player()
    elif choice == 2:
        delete_player()
    elif choice == 3:
        search_player()
    elif choice == 4:
        replace_player()
    elif choice == 5:
        show_all_players()
    elif choice == 0:
        break
    else:
        print("Invalid choice. Please try again.")
