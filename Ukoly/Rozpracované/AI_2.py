print("Zadávej čísla a nakonec zadej pouze ENTER pro ukončení zadávání")
cisla = []
while True:
    cislo = input("Zadej číslo: ")
    if cislo == "":
        break
    cisla.append(int(cislo))
seznam_trideny = sorted(cisla)
median = len(seznam_trideny) // 2
for i in cisla:
    print(f"{i} se od mediánu odlišuje o {i - seznam_trideny[median]}")