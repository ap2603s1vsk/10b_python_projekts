import random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def minesana():
    izveles = ["akmens", "šķēres", "papīrīts"]
    skaits = 0

    print(f"                                        Spēle - {bcolors.OKGREEN}AKMENS, ŠĶĒRES, PAPĪRĪT'S.{bcolors.ENDC}")
    
    while skaits < 3:
        datora_izvele = random.choice(izveles)
        mana_izvele = input("Lūdzu, izvēlieties (akmens, šķēres vai papīrīts), rakstiet 'q', lai beigt spēli: ").lower()
        
        if mana_izvele == "q":
            print(f"{bcolors.BOLD}Spēle beidzās!{bcolors.ENDC}")
        
            break
        
        if mana_izvele in izveles:
            print(f"{bcolors.OKCYAN}Dators izvēlējās:{datora_izvele}{bcolors.ENDC}")
    
            
            if mana_izvele == datora_izvele:
                print(f"{bcolors.OKGREEN}Neizšķirts!{bcolors.ENDC}")
                
            elif (mana_izvele == "akmens" and datora_izvele == "šķēres") or \
                 (mana_izvele == "šķēres" and datora_izvele == "papīrīts") or \
                 (mana_izvele == "papīrīts" and datora_izvele == "akmens"):
                print(f"{bcolors.WARNING}J Ū S   U Z V A R Ē J Ā T! 🎉 🎉 🎉{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}Jūs zaudējāt.{bcolors.ENDC}")
            skaits += 1
        else:
            print(f"{bcolors.FAIL}Drukas, vai kāda cita kļūda. Izvēlieties akmeni, šķēres vai papīru.{bcolors.ENDC}")
        
    if skaits == 3:
        print(f"{bcolors.WARNING}3 IESPEJAS IZMANTOTAS, SPĒLE BEIDZĀS! PALDIES!{bcolors.ENDC}")


minesana()
