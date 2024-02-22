person_info = [{"full_name": "Milan Sadilek", "phone_number": 777234535,
"email": "milansadilek@post.cz", "job_title": "Bussines manager", "room_number":  777,
"skype": "milan_sadilek"},
{"full_name": "Miloš Hlavatý", "phone_number": 578952487,
"email": "hlavaty@email.cz", "job_title": "developer", "room_number":  555,
"skype": "hlavac"},{'full_name': 'aa', 'phone_number': 'aa', 'email': 'aa',
                    'job_title': 'aa', 'room_number': 'aa', 'skype': 'aa'}]


def prt():
    print(("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"))
    print(person_info)
    print(("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"))
    for i in person_info:
        print(i)
prt()

delete_person = input("Enter full name of person for delete: ")
if delete_person in (for _ in person_info):
    print(delete_person)
    prt()
else:
    pass

print("Ahoj, jak se jmenuješ?")
jmeno = input()
print("Jaký jsi??")
vlastnost = input()
print(f"{jmeno} je {vlastnost}")