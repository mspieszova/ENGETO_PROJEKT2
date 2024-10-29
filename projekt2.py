"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martina Spieszová
email: mspieszova@gmail.com
discord: MartinaSpi
"""
import random
import time
cas_zacatku=time.time()
oddelovac = 32*"-"
print(f"Hi there! \n{oddelovac}")
print(f"I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.\n{oddelovac}")


#generování náhodného čísla
generovane_c=random.sample(range(10),4)
while generovane_c[0]==0:
    generovane_c=random.sample(range(10),4)
generovane_cislo=int("".join(map(str, generovane_c)))
pocet_pokusu=1

#funkce pro kontrolu
def kontrola(cisl_str):
    """
    Kontroluje, zda zadané číslo (jako string) nezačíná nulou,
    je čtyřciferné a má unikátní číslice. Vrací hodnotu True nebo False.
    
    :param cisl_str: Číslo ve formátu string zadané uživatelem.
    :type cisl_str: str
    :return: Vrací True, pokud splňuje podmínky, jinak False.
    :rtype: bool

    :Example:
    >>> kontrola("1243")
    True
    >>> kontrola("0123")
    False
    >>> kontrola("12345")
    False
    >>> kontrola("1223")
    False
    """
    if not cisl_str.isdigit():
        print(f"Číslo není číslice")
        return False            
    elif cisl_str[0] == '0':
        print("Číslo začíná nulou")
        return False
    elif len(cisl_str) != 4:
        print("Má být zadáno čtvřciferné číslo")
        return False
    elif len(set(cisl_str)) < len(cisl_str):  
        print("Číslice nejsou unikátní")
        return False
    return True


#funkce pro počítání a tisk bulls nad cows
def pocet_cow_bull(cisl_str, generovane_cislo):
    """
    Počítá a tiskne počet "bulls" a "cows" na základě zadaného čísla a generovaného čísla.
    
    "Bull" je číslice, která se nachází na správné pozici v generovaném čísle,
    zatímco "cow" je číslice, která se nachází v generovaném čísle, ale na špatné pozici.

    :param cisl_str: Zadané číslo jako string, které se má porovnat s generovaným číslem.
    :param generovaneho_cisla: Číslo ke kterému se budou počítat bull a cow
    :type cisl_str: str
    :type generovane_cislo:str
    :return: Vytiskne výsledek počtu bulls a cows. Vrací None.
    
    :Example:
    >>> generovane_c = "1234"  
    >>> pocet_cow_bull("1243")
    1 bull, 2 cows
    """
    cow = [cislice for cislice in cisl_str if int(cislice) in generovane_c]
    bull = [int(cislice) for index,cislice in enumerate(cisl_str) if int(cislice) == generovane_c[index]]
    vysledny_cow = len(cow)-len(bull)
    zapis_vysledny_cow = print(f"{vysledny_cow} {'cow' if vysledny_cow == 1 else 'cows'},{len(bull)} {'bull' if len(bull) == 1 else 'bulls'}")
    return zapis_vysledny_cow         



#samotný cyklus hry
while True:
    print(f"{oddelovac}")
    cisl_str = input(f"{'Enter a number:'if pocet_pokusu==1 else ''}")
    if kontrola(cisl_str):
        if int(cisl_str) == generovane_cislo:
                pocet_pokusu += 1
                cas_konce = time.time()
                cas_prubehu_system = cas_konce-cas_zacatku
                print(f"Correct, you've guessed the right number\nin {pocet_pokusu} guesses!")
                print(oddelovac)
                print(f"That's amazing!")        
                print(f"Time to solve it: {cas_prubehu_system :.2f}")  
                break
        else:
            pocet_cow_bull(cisl_str,generovane_c)
            pocet_pokusu += 1



        
