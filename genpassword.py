import random
import string
def genpass(l):
    return "".join(random.choices(string.ascii_letters+string.digits+"!._-",k=l))
def main():
    #TO DO Cyklus, který vygeneruje libovolný počet hesel, která budou libovolně dlouhá
    print("")
if(__name__ == "__main__"):
    main()