# Funkce pro výpis tříd
def vypis_tridy(tridy):
    for trida in tridy:
        print("-------------------------------")
        print(f'Oznaceni: {trida["Oznaceni"]}')
        print(f'Pocet zaku: {trida["Pocet zaku"]}')
        print("-------------------------------")

# Funkce pro výpsaní menu


def vypis_menu():
    print("-------------------------------")
    print("Menu")
    print("-------------------------------")
    print("1. Vypiš všechny třídy")
    print("2. Najdi a vypiš třídu")

# TO DO Funkce pro vypsání třídy
def vypis_tridu(tridy, trida):
    for t in tridy:
        if(trida == t["Oznaceni"]):
            print("-------------------------------")
            print(f'Pocet zaku: {t["Pocet zaku"]}')
            print("-------------------------------")
