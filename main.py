from colorama import *
import string
import random
import os

os = os.system
init(autoreset=True)

alphabetical = string.ascii_letters + string.digits

print(Fore.LIGHTMAGENTA_EX + f"""

      """ + Fore.LIGHTCYAN_EX + """------------------------"""+ Fore.LIGHTMAGENTA_EX +"""---------------------------""" + Fore.LIGHTCYAN_EX + """--------------------"""+ Fore.LIGHTMAGENTA_EX +"""

                                     Generator

      

                                 select 1 to generate
      
      -----------------------""" + Fore.LIGHTCYAN_EX + """--------------------------"""+ Fore.LIGHTMAGENTA_EX +"""----------------------
""")

selection = input(Style.BRIGHT + f'select: ')

if selection == '1':
    with open("generate.txt", "w") as f:
        times = int(input("how many codes: "))
        for i in range(times):
            random_alphabetical = ''.join(random.choice(alphabetical) for i in range(16))
            code = "https://discord.gift/" + random_alphabetical
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f"Generated {i + 1} / {times}")
            f.write(code + "\n")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f"Opening the txt file.")
    os("generate.txt")
    input(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + f"Press to exit.")
else:
    print(f'Invalid Selection, Please Try Again!')