from funkce import vypis_tridu, vypis_tridy
from funkce import vypis_menu
def main():
    tridy = [
        {"Oznaceni": "IT1A", "Pocet zaku": 17},
        {"Oznaceni": "IT1B", "Pocet zaku": 16},
        {"Oznaceni": "IT2A", "Pocet zaku": 17},
        {"Oznaceni": "IT2B", "Pocet zaku": 17},
        {"Oznaceni": "IT3", "Pocet zaku": 13},
        {"Oznaceni": "IT4", "Pocet zaku": 14},
    ]
    vypis_menu()
    volba = int(input("Vyber možnost ze seznamu: "))
    match volba:
        case 1:
            vypis_tridy(tridy)
        case 2:
            trida=str(input("Zadej třídu: "))
            vypis_tridu(tridy, trida)
        case _:
            print("Tato možnost nexistuje!")
if(__name__ == "__main__"):
    main()
