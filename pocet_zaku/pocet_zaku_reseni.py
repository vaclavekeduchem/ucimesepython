def main():
    tridy = [
        {"Oznaceni": "IT1A", "Pocet zaku": 17},
        {"Oznaceni": "IT1B", "Pocet zaku": 16},
        {"Oznaceni": "IT2A", "Pocet zaku": 17},
        {"Oznaceni": "IT2B", "Pocet zaku": 17},
        {"Oznaceni": "IT3", "Pocet zaku": 13},
        {"Oznaceni": "IT4", "Pocet zaku": 14},
    ]
    for trida in tridy:
        print("-------------------------------")
        print(f'Oznaceni: {trida["Oznaceni"]}')
        print(f'Pocet zaku: {trida["Pocet zaku"]}')
        print("-------------------------------")
if(__name__ == "__main__"):
    main()
