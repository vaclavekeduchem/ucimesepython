import random
import string
from tabulate import tabulate
def genpass(l : int):
    return "".join(random.choices(string.ascii_letters+string.digits+"!._-",k=l))
def writepasswords(passwords : list, password_file_path : str):
    password_file = open(password_file_path, 'wt')
    password_file.write(tabulate(passwords, headers=["ID", "Heslo"], numalign='center', tablefmt='simple'))
    password_file.close()
def main():
    #TO DO Cyklus, který vygeneruje libovolný počet hesel, která budou libovolně dlouhá
    pocet_hesel = int(input('Počet hesel: '))
    delka_hesel = int(input('Délka hesel: '))
    hesla = []
    for i in range(pocet_hesel):
        hesla.append([
            i+1,
            genpass(delka_hesel)
        ])
    print(tabulate(hesla, headers=["ID", "Heslo"], numalign='center', tablefmt='grid'))
    writepasswords(hesla, './hesla.txt')
if(__name__ == "__main__"):
    main()