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


while True:
   menu = """
    1 = add player
    2 = delete player
    3 = search player
    4 replace player
    5 = END"""
    print(menu)
    print(f"Great basketball players: \n {players} ")

    choice = int(input("Your choice is: "))

    if choice == 1:
        add()
    if choice == 2:
        delete()
