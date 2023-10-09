import os
import time
from balance import Balance
from deposite import Debosite
from tranfer import tranfermoney
from emblem import em
def cont():
    while True:
      ask = input("[*] If you want to continue (y/n) :")
      if ask == 'y':
         os.system('cls' if os.name == 'nt' else 'clear')
         em()
         return menulist()
      elif ask =='n':
          print("Thank you for using our bank")
          time.sleep(0.5)
          exit()
def menulist():
    print("[...] SELECT SERVICES [...]")
    print('''
             [1] Debosite
             [2] Money transfer
             [3] Balance Check
             [4] exit
                                           
          ''')
    select = input("[*] Service :")
    if select == '1':
        Debosite()
    
        return cont()

    elif select == '2':
        tranfermoney()
     
        return cont()

    elif select == '3':
        Balance()
    
        return cont()
    else:
        print("Thank you for using our bank...")
        time.sleep(0.5)
        exit()
