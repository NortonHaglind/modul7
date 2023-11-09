
from msvcrt import getwch
import os
from time import sleep
from colors import bcolors 

os.system("cls")


for i in range (10):
    print(bcolors.RED + f"fafa")
    sleep(1.5)
    os.system("cls")
    print(bcolors.BLUE + f"fafa")
    sleep(1.5)
    os.system("cls")

active=True

while active:
    name=input(bcolors.YELLOW + f"vad heter du? ")

    if name=="":
       print(f"skriv namn") 
       continue

        
    while True:
        try:
            age=float(input(bcolors.YELLOW + f"Hur gammal är du? "))
            break
        except:
            print(bcolors.RED + f"du skrev fel")
            continue
    print(bcolors.BLUE + f"Hej {name} välkommen till mitt program. Du är {age} gammal.")
    while True:
        print(bcolors.YELLOW + f"är det här rätt? y/n")
        question=getwch()
        if question=="y":
            print(bcolors.BLUE + f"Hej {name} välkommen till mitt program. Du är {age} gammal.")
            active=False
            break
        elif question=="n":
            break
      

    