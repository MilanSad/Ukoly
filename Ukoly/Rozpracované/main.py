

"""Create an app Company. Store the following information
about a person: full name, phone number, corporate email,
job title, room number, skype. Provide the possibility to add,
delete, search, and replace data. Use a dictionary to store
information."""

person_info = [{"full_name": "Milan Sadilek", "phone_number": 777234535,
"email": "milansadilek@post.cz", "job_title": "Bussines manager", "room_number":  777,
"skype": "milan_sadilek"},
{"full_name": "Miloš Hlavatý", "phone_number": 578952487,
"email": "hlavaty@email.cz", "job_title": "developer", "room_number":  555,
"skype": "hlavac"}]



full_name = "aaaaa"
phone_number = 123456
email = "my email: "
job_title = "good job: "
room_number = 555
skype = "skyyyype"

# full_name, phone_number, email, job_title, room_number, skype


person_info.append({"full_name": full_name, "phone_number": phone_number,
"email": email, "job_title": job_title, "room_number": room_number, "skype": skype})
print(person_info)

for i in person_info:
    print(i)

#({[full_name] = new_full_name})