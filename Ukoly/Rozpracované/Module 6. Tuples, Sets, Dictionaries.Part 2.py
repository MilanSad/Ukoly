"""


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


players = {"Milan": 178, "Robert": 185, "Richard": 186}


def add():
    full_name = input("Enter name of player: ")
    height = int(input("Enter height of player: "))
    players[full_name] = height


def delete():
    delete_item = input("Enter name for delete: ")
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
    search_name = input("Enter search name: ")
    new_height = input("Enter new height: ")
    if search_name in players:
        players[search_name] = new_height
    else:
        print(f"{search_name} isn´t in Great basketball players.")

while True:
    menu = (
        
#todo 
    )
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


Task 2
Create an app English-French Dictionary. Store a word
in English and its French translation. Provide the possibility
to add, delete, search, and replace data. Use a dictionary to
store information.


dictionary = {"Hello": "Bonjour", "and": "at"}


def add(english_word, french_word):
    dictionary[english_word] = french_word


def delete(del_item):
    dictionary.pop(del_item)


def search():
    search_word = input("Enter search word: ")
    if search_word in dictionary:
        print(f"{search_word} in French is: {dictionary.get(search_word)} ")
    else:
        print(f"{search_word} isn´t in dictionary.")


def print_dictionary():
    print(f"English-French Dictionary: \n {dictionary}")


def replace():
    english_word = input("Enter English word: ")
    if english_word in dictionary:
        new_french_word = input("Enter new French word: ")
        dictionary[english_word] = new_french_word
    else:
        print(f"{english_word} isn´t in dictionary")


while True:
    menu = (
        # todo
 #   1 = add player
  #  2 = delete player
   # 3 = search player
   # 4 = replace player
   # 5 = END
    )
    print()
    print_dictionary()
    print(menu)
    try:
        choice = int(input("Your choice is (1-5): "))
    except ValueError:
        print("Choice only number 1 -5 !!!")
        continue

    if choice >= 0 or choice <= 5:
        if choice == 1:
            english_word = input("Enter English word: ")
            french_word = (input("Enter French word: "))
            add(english_word, french_word)

        if choice == 2:
            delete_item = input("Enter English for delete: ")
            if delete_item in dictionary:
                delete(delete_item)
            else:
                print(f"{delete_item} is in´t in dictionary")

        if choice == 3:
            search()

        if choice == 4:
            replace()
        if choice == 5:
            break
    else:
        print("Bad choice")

"""
"""
Task 3
Create an app Company. Store the following information
about a person: full name, phone number, corporate email,
job title, room number, skype. Provide the possibility to add,
delete, search, and replace data. Use a dictionary to store
information.
"""