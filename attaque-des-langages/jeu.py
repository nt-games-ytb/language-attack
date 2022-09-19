#region Import modules
import time
import os
from colorama import Fore, Back, Style
import joueur
import village
try:
    from playsound import playsound
except:
    print(f"{Fore.RED}Nous avons remarqué que vous n'avez pas le module \"Playsound\" !\nNous allons donc vous l'installer :")
    os.system("pip install playsound")
    from playsound import playsound
#endregion

dossier = os.path.dirname(os.path.realpath(__file__))

def afficher(textes, temps, couleur): #Manque le son
    assert type(textes) == list

    #Old : print(f"{Fore." + couleur + "}") #Couleur du texte

    for phrase in range(len(textes)):
        for caractère in range(len(textes[phrase])):
            #region Couleur
            if couleur == "rouge":
                print(f"{Fore.RED}", end="")
            elif couleur == "jaune":
                print(f"{Fore.YELLOW}", end="")
            elif couleur == "vert":
                print(f"{Fore.GREEN}", end="")
            elif couleur == "cyan":
                print(f"{Fore.CYAN}", end="")
            elif couleur == "bleu":
                print(f"{Fore.BLUE}", end="")
            elif couleur == "magenta":
                print(f"{Fore.MAGENTA}", end="")
            elif couleur == "blanc":
                print(f"{Fore.WHITE}", end="")
            elif couleur == "normal":
                print(f"{Fore.RESET}", end="")
            else:
                print("Couleur inconnue !")
                pass
            #endregion
            print(textes[phrase][caractère], end="")
            #playsound(dossier + "\\afficher.mp3") #Désactiver car trop lent
            time.sleep(temps)
        if phrase != len(textes) - 1:
            print()

    print(f"{Style.RESET_ALL}") #Remettre le texte normal

def creation_de_joueur():
    pass

def tutoriel():
    pass

#print(f"{Back.BLACK}") #à voir plus tard
village_utilisé = village.Village()
if os.path.isfile(dossier + "\sauvegarde.xml") == True: #Si il n'y a pas de sauvegarde
    afficher([
    "Bonjour et bienvenue dans le jeu !",
    "Je vois que tu es nouveau, je me suis permit de fouiller dans ton PC et je n'ai pas trouvé de sauvegarde du jeu.",
    "Enfin bref, moi c'est M.Mathieu ancien prof d'NSI au lycée Thierry Maulnier et actuelle prof d'NSI dans le Nord et fier d'y être parce que j'en pouvais plus de ces fous de 1G03."], 0, "normal")#blanc
    print()
    village_utilisé.Texte_de_Mathieu()
    afficher(["Parle, moi un peu d'toi que jte créer un perso pour que tu joue :"], 0, "normal")#blanc
    nom_du_joueur = input("Comment tu t'appelle ? ")
    joueur_actuel = joueur.Joueur(nom_du_joueur, 100, 100, 0, 0, 1, 0, ["print"], 0, 0.1)
else:
    print("a")
#jeu = True
#while jeu == True:
    #print()