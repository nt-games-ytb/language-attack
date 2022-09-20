#region Import modules
import time
import os
import xml.dom.minidom
from colorama import Fore, Style
import joueur
import village

try:
    from playsound import playsound
except:
    print(f"{Fore.RED}Nous avons remarqué que vous n'avez pas le module \"Playsound\" !\nNous allons donc vous l'installer :")
    os.system("pip install playsound")
    from playsound import playsound
#endregion

village_utilisé = village.Village(True, True, True, True)
joueur_actuel = joueur.Joueur("", 100, 100, 0, 0, 0, 1, 0, ["print"], 0, 0.05, os.path.dirname(os.path.realpath(__file__)),"\sauvegarde.xml")

class Initialisation:
    def __init__(self, dossier):
        self.dossier = dossier

    def fichier_existe(self, fichier):
        if os.path.isfile(self.dossier + "\\" + fichier) == True:
            return True
        else:
            return False

    def creation_de_la_sauvegarde(self):
        afficher([
        "Bonjour et bienvenue dans le jeu !",
        "Je vois que tu es nouveau, je me suis permit de fouiller dans ton PC et je n'ai pas trouvé de sauvegarde du jeu.",
        "Enfin bref, moi c'est M.Mathieu ancien prof d'NSI au lycée Thierry Maulnier et actuelle prof d'NSI dans le Nord et fier d'y être parce que j'en pouvais plus de ces fous de 1G03."], 0.05, "normal")
        print()
        fichier = open(self.dossier + "\sauvegarde.xml", "a")
        fichier.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<sauvegarde>\n\n</sauvegarde>")
        fichier.close()

    def creation_de_joueur(self):
        village_utilisé.Texte_de_Mathieu()
        afficher(["Parle, moi un peu d'toi que jte créer un perso pour que tu joue :"], 0.05, "normal")
        joueur_actuel.nom = input("Comment tu t'appelle ? ")
        self.sauvegarder(self.dossier + joueur_actuel.fichier_de_sauvegarde, joueur_actuel)

    def afficher_les_joueurs(self, fichier):
        print("Un fichier de sauvegarde a été trouvé !")
        print("Plusieurs options s'offre donc à toi, elle sont les suivantes :")
        print("0 - Créer un nouveau joueur")
        #pour chaque joueur : print(nombre + " - Jouer avec " + nom_du_joueur) 
        fichier_de_sauvegarde = xml.dom.minidom.parse(self.dossier + fichier)
        joueurs = fichier_de_sauvegarde.getElementsByTagName("joueur")
        for nom in joueurs:
            print(nom.getAttribute("nom"))
        #à finir ou changer
        pass

    def chargement_du_joueur(self, fichier, numéro_du_joueur):
        #Essaye de convertir numéro en int sinon dit que c'est pas bon 
        #puis charge le joueur
        pass

    def sauvegarder(self, fichier, joueur):
        pass

#region Affichage
def afficher(textes, temps, couleur): #Manque le son
    assert type(textes) == list
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

def saut_de_lignes():
    print()
#endregion

#region Tutoriel
def scenario():
    print("Voici le scènario...")

def demande_tutoriel():
    print("Veux-tu lancer le tutoriel ?\n1 - Oui | 2 - Non")
    réponse_tutoriel = input()
    if réponse_tutoriel == "1":
        print("D'accord, on lance le tutoriel !")
        saut_de_lignes()
        tutoriel()
    elif réponse_tutoriel == "2":
        print("D'accord, on passe le tutoriel !")
        saut_de_lignes()
    else:
        print("Je vais prendre cette réponse pour un non, donc on passe le tutoriel !")
        saut_de_lignes()
    

def tutoriel():
    print("Voici le tutoriel...")
#endregion

#region Séléction du joueur
jeu = Initialisation(joueur_actuel.dossier_du_jeu) #Créer jeu, un objet de la class initailisation qui prend comme attribut le dossier "attaque-des-langages"
if jeu.fichier_existe("sauvegarde.xml") == False: #Si il n'y a pas de sauvegarde
    #jeu.creation_de_la_sauvegarde()
    saut_de_lignes()
    jeu.creation_de_joueur()
    saut_de_lignes()
    scenario()
    saut_de_lignes()
    demande_tutoriel()
    saut_de_lignes()
else:
    jeu.afficher_les_joueurs("\sauvegarde.xml")
    numéro_du_joueur = input("Quelle option choisis-tu ? ")
    jeu.chargement_du_joueur("\sauvegarde.xml", numéro_du_joueur)
    village_utilisé.première_fois_village = False
    village_utilisé.première_fois_hopital = False
    village_utilisé.première_fois_banque = False
    village_utilisé.première_fois_shop = False
#endregion

#region Jeu
jeu = True
while jeu == True:
    if village_utilisé.première_fois_village == True:
        village_utilisé.Texte_de_Mathieu()
        afficher(["Je te présente le village, c'est là où tu habite.",
        "On y trouve un hopital pour se soigner, une banque pour stocker ton argent et un shop pour acheter des armes.",
        "Tu peux aussi partir dans une zone pour aller battre les différents langages."], joueur_actuel.vitesse_du_texte, "normal")
        village_utilisé.première_fois_village = False
        saut_de_lignes()
        
    village_utilisé.village(joueur_actuel)
        
    pass
#endregion