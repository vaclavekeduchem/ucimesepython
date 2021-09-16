
a=input("První číslo: ")
o=input("Jakou operaci chceš provést: ")
b=input("Druhé číslo: ")
match o:
    case "+":
        vysledek=int(a)+int(b)
    case "-":
        vysledek=int(a)-int(b)
    case "*":
        vysledek=int(a)*int(b)
    case "/":
        vysledek=int(a)/int(b)
    case _:
        print("Operace nexistuje")
        exit()
print(a+o+b+"="+str(vysledek))
input("")