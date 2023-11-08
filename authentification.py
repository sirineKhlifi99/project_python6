import hashlib
import maskpass

import certificat
import hashage
import rsa

def authentifier():
    a=input("entrer votre email: ")
    b=maskpass.askpass(mask="")
    b=hashlib.sha256(b.encode()).hexdigest()
    with open('fenregistrement.txt' ,'r') as file:
        lines = file.readlines()
        for line in lines :
            line = line.strip('\n')
            if  line == (f"{a};{b}") :
                print(f"Bienvenue {a} vous etes authentifier ")
                menuS()
                break
        else:
            print("Merci de verifier le login/mot de pass ?")





def menuauthentification():
    import pyfiglet
    import colorama
    print(colorama.Fore.RED)
    banner = pyfiglet.figlet_format("AUTHENTIFICATION", font="small")
    print(banner)
    while True :
        print("1- S'authentifier")
        print("2- Quitter")

        choix = input('Donnez votre choix : ')
        match choix:
            case '1':
                authentifier()
            case '2':
                break
            case _:
                print("Merci d'introduire soit 1 ou 2 pour quitter")

def menuS():
    while True:
        print("**********Vous êtes authentifié, vous pouvez passer a l'étape suivante **********")
        print(" 1- Donnez un mot à haché (en mode invisible)")
        print(" 2- Chiffrement (RSA)")
        print(" 3- Certificat (RSA)")
        print(" 4- Quitter")
        choix = int(input("Donnez votre choix :"))
        match choix:
            case '1':
                hashage.mHachage()
            case '2':
                rsa.mrsa()
            case '3':
                certificat.menuCer()
            case '4':
                break
            case _:
                print("choix invalid \n Merci d'introduire 1,2,3 ou bien 4 pour quitter")

