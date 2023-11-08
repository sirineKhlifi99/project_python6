import re
import string
import maskpass
import hashlib

def verifemail(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True

def verifpwd(pwd):
    if len(pwd) >=8:
        if any(car in string.digits for car in pwd):
            if any(car in string.ascii_uppercase for car in pwd):
                if any(car in string.ascii_lowercase for car in pwd):
                    if any(car in string.punctuation for car in pwd):
                        return True
                    else:
                        print("au min un cart spécial")
                else:
                    print("au minimum une lettre miniscule")
            else:
                print("Au min une lettre maj")
        else:
            print("Au min un numérique")
    else:
        print("long == 8 ")
def exist(email):
    with open("fenregistrement.txt", "r") as file:
        lines = file.readlines()
        for line in lines :
            line = line.strip('\n')
            e=line.split(';')
            if  e[0] == email :
                return False
        file.close()
        return True
def enregistrer():
    import pyfiglet
    import colorama
    print(colorama.Fore.RED)
    banner = pyfiglet.figlet_format("ENREGISTREMENT", font="small")
    print(banner)
    while True :
        email=input("Donnez votre email : ")
        if verifemail(email) :
            if  exist(email):
                while True:
                    p = maskpass.askpass(mask="")
                    if verifpwd(p):
                        p=hashlib.sha256(p.encode()).hexdigest()
                        with open("fenregistrement.txt","a") as file:
                            file.write(f"{email};{p}\n")
                            print(f"Compte de {email} creé avec succès")
                            from main import menu
                            print("#################"
                                  "#Menu principal#"
                                  "################")
                            menu()
                            break
                    else:
                        print("merci de respecter les critére")
                break
            else:
                print("Votre Email est déja utiliser")
        else :
            print("Merci d'introduire un email valide ")


