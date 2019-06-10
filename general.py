import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def showMsg(txt, clear=True):
    if clear:
        cls()

    print(txt)