"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Matouš Kopáček
email: matouskopacek@gmail.com
discord: matousk_84638
"""

import random
import time

line = "-" * 50

def nahodne_cislo_hry():
    """Funkce, která vygeneruje náhodné 4 místné číslo s tím, že první číslo nebude 0 a číslo bude unikátní."""
    nahodne_cislo = str(random.randint(1,9))
    while len(nahodne_cislo) != 4:
        cislo = random.randint(0,9)
        if str(cislo) in nahodne_cislo:
            continue
        else:
            nahodne_cislo += str(cislo)
    return nahodne_cislo

cislo_hry = nahodne_cislo_hry()

def overeni_cisla(user_cislo):
    """Funkce ověřuje správně zadané číslo uživatele."""
    if user_cislo[0] == "0" or not user_cislo.isnumeric() or len(user_cislo) > 4 or len(user_cislo) < 4:
        return "Invalid number or character for this game."
    elif len(set(user_cislo)) != 4:
        return "Number is not uniqe..."


def bulls_and_cows():
    print("Hi there!")
    print(line)
    print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
    print(line)
    print("Enter a number:")
    
    zacatek_hry = time.time()
    game = True
    pokusy = 0

    while game:
        print(line)
        cows = 0
        bulls = 0
        user_cislo = input(">>> ")
        neplatny_vstup = overeni_cisla(user_cislo)
        if overeni_cisla(user_cislo):
            print(neplatny_vstup)
            continue
        
        for index, cislice in enumerate(user_cislo):
            if cislice in cislo_hry:
                if cislice == cislo_hry[index]:
                    bulls += 1
                else:
                    cows += 1
        
                    
        print(f"{bulls} bulls, {cows} cows")              
        
        pokusy += 1
        if bulls == 4:
            konec_hry = time.time()
            cas_hry = konec_hry - zacatek_hry
            minuty = int(cas_hry // 60)
            sekundy = int(cas_hry % 60)
            if minuty == 0:
                print(f"Correct, you've guessed the right number in {pokusy} guesses in {sekundy} seconds!") 
            else:
                print(f"Correct, you've guessed the right number in {pokusy} guesses in {minuty} minutes and {sekundy} seconds!") 
            game = False

bulls_and_cows()
    
      









  

