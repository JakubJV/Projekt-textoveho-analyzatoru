from pprint import pprint

"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jakub Vondra
email: jakubvond@seznam.cz
discord: JakubJv #7166
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


oddelovac = "-" * 37
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "123"}

username = input("Zadej své přihlašovací jméno: ")
password = input("Zadej své heslo: ")

if users.get(username) == password:
    print(f"Vítej v naší aplikaci, {username}.")
    print(f"Máme k analýze 3 texty.")
    print(oddelovac)


else:
    print("Nezaregistrovaný uživatel, ukončuji program..")
    quit()


vyber_textu = input(f"Vyber si číslo textu k analýze: ")

if vyber_textu.isnumeric():
    vyber_textu_cislo = int(vyber_textu)
else:
    print("Nezadal jsi číslo. Ukončuji program...")
    quit()

if vyber_textu_cislo in range(1, 4):
    vybrany_text = TEXTS[vyber_textu_cislo - 1]
    print(f"VYBRANÝ TEXT: {vybrany_text} ")
else:
    print("Zadané číslo textu není k dispozici! Ukončuji program..")
    quit()

print(oddelovac)

vycistena_slova = []

for slovo in vybrany_text.split():
    ciste_slovo = slovo.replace(".", "")
    vycistena_slova.append(ciste_slovo)

ciste_slovo = len(vycistena_slova)

# print(vycistena_slova) -  pro orientaci

vyskyt_slov = {}


for slovo in vycistena_slova:
    if slovo not in vyskyt_slov:
        vyskyt_slov[slovo] = 1
    else:
        vyskyt_slov[slovo] += 1

pocet_slov = len(vycistena_slova)


if slovo in vybrany_text:
    print(f"Ve zvoleném textu je {pocet_slov} slov.")
else:
    quit()

slova_zacinajici_velkym = {}

for slovo in vyskyt_slov:
    if slovo.istitle():
        slova_zacinajici_velkym[slovo] =+ 1

pocet_slov_zacinajici_velkym = len(slova_zacinajici_velkym)

if slovo in vybrany_text:
    print(f"Ve zvoleném textu je {pocet_slov_zacinajici_velkym} slov začínajících velkým písmenem.")
else:
    quit()

slova_velkym_pismem = {}

for slovo in vyskyt_slov:
    if slovo.isupper() and slovo.isalpha():     # přidat: slovo.isalpha() započítavalo např.: 30N z prvního textu
        slova_velkym_pismem[slovo] =+ 1

pocet_slov_velkym = len(slova_velkym_pismem)

if slovo in vybrany_text:
    print(f"Ve zvoleném textu je {pocet_slov_velkym} slov velkým písmenem.")
else:
    quit()


slova_malym = 0


for klic, hodnota in vyskyt_slov.items():
    # print(klic) - moje pro orientaci
    if klic.islower():
        slova_malym += hodnota


if slovo in vybrany_text:
    # print(f"Ve zvoleném textu je {pocet_slov_malym} slov malým písmem.")
    print(f"Ve zvoleném textu je {slova_malym} slov malým písmem.")
else:
    quit()

cisla = {}

for slovo in vyskyt_slov:
    if slovo.isnumeric():
        cisla[slovo] = +1

pocet_cisel = len(cisla)

if slovo in vybrany_text:
    print(f"Ve zvoleném textu je {pocet_cisel} číslo.")
else:
    quit()


soucet = 0

for slovo in vyskyt_slov:
    if isinstance(slovo, int) or slovo.isdigit():
        soucet += int(slovo)

print(f"Součet všech čísel v textu je {soucet}.")
print(oddelovac)

frekvence_slov = sorted(list(vyskyt_slov.values()))

word_freq = []

for slovo in vyskyt_slov.keys():
    pocet_vyskytu = vyskyt_slov[slovo]
    if pocet_vyskytu in frekvence_slov:
        word_freq.append((pocet_vyskytu, slovo))


word_freq = sorted(word_freq)


for index, pocet_a_slovo in enumerate(word_freq, 1):
    print(oddelovac,
          f"{index}|{pocet_a_slovo[1]:^12}|{pocet_a_slovo[0]}x|",
          sep="\n")
else:
    print(oddelovac)