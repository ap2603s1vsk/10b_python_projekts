import random
import time

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

simboli = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']

def minesana():
    izveles = ["akmens", "šķēres", "papīrīts"]
    skaits = 0
    uzvaras_lietotajs = 0
    uzvaras_dators = 0





    print(f"                Spēle - {bcolors.OKGREEN}AKMENS, ŠĶĒRES, PAPĪRĪT'S.{bcolors.ENDC}")
    print()
    print("Spēle tiek spēlēta ar datoru, tai ir 3 raundi.")
    print("Pēc katra raunda tiek noteikts - zaudē, vinnē vai ir neizšķirts.")
    print("Beigās punkti tiek saskaitīti un pateikts rezultāts.")
    print()

    while skaits < 3:
        datora_izvele = random.choice(izveles)
        mana_izvele = input("Izvēlieties (akmens, šķēres vai papīrīts), raksti 'q', lai beigt spēli: ").lower()
        
        if mana_izvele == "q":
            print(f"{bcolors.BOLD}Spēle beidzās!{bcolors.ENDC}")
        
            break
        
        
        i = 0
        while True:
            i = (i + 1) % len(simboli)
            print('\r\033[K%s Dators domā, uzgaidi!' % simboli[i], flush=True, end='')
            time.sleep(0.1)
            if random.random() < 0.02:
                break
        print('\r\033[K', end='')  # apstādina animāciju


        if mana_izvele in izveles:
            print(f"Dators izvēlējās:{bcolors.OKCYAN}{datora_izvele}{bcolors.ENDC}")
    
            
            if mana_izvele == datora_izvele:
                print(f"{bcolors.OKBLUE}NEIZŠĶIRTS!{bcolors.ENDC}")
                



            elif (mana_izvele == "akmens" and datora_izvele == "šķēres") or \
                 (mana_izvele == "šķēres" and datora_izvele == "papīrīts") or \
                 (mana_izvele == "papīrīts" and datora_izvele == "akmens"):
                print(f"{bcolors.OKGREEN}JŪS UZVARĒJĀT! 🎉 🎉 🎉{bcolors.ENDC}")
                uzvaras_lietotajs += 1
            
            
            
            else:
                print(f"{bcolors.FAIL}JŪS ZAUDĒJĀT, varbūt paveiksies nakamreiz.{bcolors.ENDC}")
                uzvaras_dators += 1
            
            skaits += 1

        else:
            print(f"{bcolors.FAIL}Drukas, vai kāda cita kļūda.{bcolors.ENDC} Izvēlieties akmens, šķēres vai papīrīt's.")
            

        
        
    if skaits == 3:
        print()
        print(f"{bcolors.OKCYAN}            APSVEICU! 3 spēles raundi beidzās!{bcolors.ENDC}")
        print()
        

        if uzvaras_lietotajs > uzvaras_dators:
            
            print(f"{bcolors.WARNING}YEEEEY Jūs uzvarējāt ar rezultātu: {uzvaras_lietotajs} - {uzvaras_dators}!{bcolors.ENDC}")


        elif uzvaras_dators > uzvaras_lietotajs:
            print(f"{bcolors.FAIL}VISS SLIKTI - Dators uzvarēja ar rezultātu: {uzvaras_dators} - {uzvaras_lietotajs}!{bcolors.ENDC}")


        else:
            print(f"Rezultāts ir {bcolors.OKBLUE}NEIZŠĶIRTS!{bcolors.ENDC}")
    
    
    print()        
    vel = input(f"{bcolors.OKGREEN}Ieraksti 'jā', lai spēle sāktos no jauna! Veiksmi! Raksti 'nē', lai beigt : {bcolors.ENDC}")
    if vel == "jā":
        minesana()
    if vel == "nē":
        print(f"{bcolors.OKCYAN}Uzredzēšanos!!{bcolors.ENDC}")

                
    
   



minesana()
