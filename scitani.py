stavcyklu=1
celkem=0
while(stavcyklu):
    y=input("Zadej číslo: ")
    if(y != "00"):
        celkem += int(y)
        print(celkem)
    else:
        stavcyklu=0
        exit