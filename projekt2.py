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
pocet_pokusu=0

#funkce pro kontrolu
def kontrola(cisl_str):
    """
    
    
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


#    funkce pro počítání a tisk bulls nad cows
def pocet_cow_bull(cisl_str):         
    bull = [cislice for cislice in cisl_str if int(cislice) in generovane_c]
    cow = [int(cislice) for index,cislice in enumerate(cisl_str) if int(cislice)==generovane_c[index]]
    vysledny_bull = len(bull)-len(cow)
    zapis_vysledny_bull = print(f"{vysledny_bull} {'bull' if vysledny_bull==1 else 'bulls'},{len(cow)} {'cow' if len(cow)==1 else 'cows'}")
    return zapis_vysledny_bull            



#samotný cyklus hry
while True:
    pocet_pokusu += 1
    cisl_str = input(f"{oddelovac}\n")
    if kontrola(cisl_str):
        if int(cisl_str) == generovane_cislo:
                cas_konce = time.time()
                cas_prubehu_system = cas_konce-cas_zacatku
                print(f"Correct, you've guessed the right number\nin {pocet_pokusu} guesses!")
                print(oddelovac)
                print(f"That's amazing!")        
                print(f"Time to solve it: {cas_prubehu_system :.2f}")  
                break
        else:
            pocet_cow_bull(cisl_str)

    



        
