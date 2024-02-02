"""
Task 2
Create an app English-French Dictionary. Store a word
in English and its French translation. Provide the possibility
to add, delete, search, and replace data. Use a dictionary to
store information.
Task 3
Create an app Company. Store the following information
about a person: full name, phone number, corporate email,
job title, room number, skype. Provide the possibility to add,
delete, search, and replace data. Use a dictionary to store
information.
Task 4
Create an app Book Collection. Store the following information
about books: author, title, genre, year of release,
publisher. Provide the possibility to add, delete, search, and
replace data. Use a dictionary to store information.
"""

"""
Task 1
Create an app that stores information about great basketball
players. Store the player’s full name and height. Provide
the possibility to add, delete, search, and replace data. Use
a dictionary to store information.
"""

players = {"Milan": 178, "Robert": 185, "Richard": 186}


def add():
    full_name = input("Enter name of player: ")
    height = int(input("Enter height of player: "))
    players[full_name] = height


def delete():
    delete_item = input("Enter name for delete")
    players.pop(delete_item)


def search():
    search_name = input("Enter search name: ")
    if search_name in players:
        print(f"{search_name} is in Great basketball players.")
    else:
        print(f"{search_name} isn´t in Great basketball players.")


def print_players():
    print(f"Great basketball players: \n {players},\n {menu} ")


def replace():
    replace_name = input("Enter search name: ")
    replace_height = input("Enter search name: ")
#todo    if replace_player in players:
#todo        players[]
#todo    else:
#todo        print(f"{replace_player} isn´t in Great basketball players.")

while True:
    menu = (
        """
    1 = add player
    2 = delete player
    3 = search player
    4 = replace player
    5 = END
    """)
    print()
    print_players()

    choice = int(input("Your choice is: "))

    if choice == 1:
        add()
    if choice == 2:
        delete()
    if choice == 3:
        search()
    if choice == 4:
        replace()
    if choice == 5:
        break
