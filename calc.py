def main():
    x=int(input("Zadej první číslo: "))
    o=input("* / + -: ")
    y=int(input("Zadej druhé číslo: "))
    match o:
        case "+":
           print(f"{x} + {y} = {x+y}")
        case "-":
            print(f"{x} - {y} = {x-y}")
        case "*":
            print(f"{x} * {y} = {x*y}")
        case "/":
            print(f"{x} / {y} = {x/y}")
        case _:
            print("Neznámá operace") 
if(__name__ == "__main__"):
    main()