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
joueur_actuel = joueur.Joueur("", 100, 100, 0, 0, 0, 1, 0, ["print"], 0, 0.05, os.path.dirname(os.path.realpath(__file__)), "\sauvegarde.xml")

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
        fichier = open(self.dossier + "\sauvegarde.xml", "a")
        fichier.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<sauvegarde>\n</sauvegarde>")
        fichier.close()

    def creation_de_joueur(self):
        village_utilisé.Texte_de_Mathieu()
        afficher(["Parle, moi un peu d'toi que jte créer un perso pour que tu joue :"], 0.05, "normal")
        joueur_actuel.nom = input("Comment tu t'appelle ? ")
        self.sauvegarder()

    def afficher_les_joueurs(self, fichier):
        print("Un fichier de sauvegarde a été trouvé !")
        print("Plusieurs options s'offre donc à toi, elle sont les suivantes :")
        print("0 - Créer un nouveau joueur")
        fichier_xml_de_sauvegarde = xml.dom.minidom.parse(self.dossier + fichier)
        liste_des_joueurs = fichier_xml_de_sauvegarde.documentElement.getElementsByTagName("joueur")
        numéro_joueur = 1
        for nom in liste_des_joueurs:
            print(str(numéro_joueur) + " - Jouer avec " + nom.childNodes[0].nodeValue)
            numéro_joueur = numéro_joueur + 1
        if numéro_joueur == 1:
            print(f"{Fore.RED}Malheuresement, nous n'avons pas réussi à charger de joueurs.{Fore.RESET}")

    def chargement_du_joueur(self, fichier, numéro_du_joueur):
        if numéro_du_joueur == 0:
            self.creation_de_joueur()
        else:
            fichier_xml_de_sauvegarde = xml.dom.minidom.parse(self.dossier + fichier)
            liste_des_joueurs = fichier_xml_de_sauvegarde.documentElement.getElementsByTagName("joueur")
            joueur_actuel.nom = liste_des_joueurs[numéro_du_joueur - 1].childNodes[0].nodeValue
            joueur_actuel.vie = int(liste_des_joueurs[numéro_du_joueur - 1].getAttribute("vie"))
            joueur_actuel.vie_maximal = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("vie_maximal")
            joueur_actuel.argent = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("argent")
            joueur_actuel.argent_banque = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("argent_banque")
            joueur_actuel.expérience = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("experience")
            joueur_actuel.niveau = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("niveau")
            joueur_actuel.objet_en_main = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("objet_en_main")
            joueur_actuel.sac = list(liste_des_joueurs[numéro_du_joueur - 1].getAttribute("sac"))
            joueur_actuel.langage_débloqué = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("langage_debloque")
            joueur_actuel.vitesse_du_texte = float(liste_des_joueurs[numéro_du_joueur - 1].getAttribute("vitesse_du_texte"))
            joueur_actuel.dossier_du_jeu = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("dossier_du_jeu")
            joueur_actuel.fichier_de_sauvegarde = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("fichier_de_sauvegarde")

    def sauvegarder(self):
        fichier_xml_de_sauvegarde = xml.dom.minidom.parse(joueur_actuel.dossier_du_jeu + joueur_actuel.fichier_de_sauvegarde)
        liste_des_joueurs = fichier_xml_de_sauvegarde.documentElement.getElementsByTagName("joueur")
        for nom in liste_des_joueurs:
            if nom.childNodes[0].nodeValue == joueur_actuel.nom:
                #Faut que sa les changes
                nom.setAttribute("vie", joueur_actuel.vie)
                nom.setAttribute("vie_maximal", joueur_actuel.vie_maximal)
                nom.setAttribute("argent", joueur_actuel.argent)
                nom.setAttribute("argent_banque", joueur_actuel.argent_banque)
                nom.setAttribute("experience", joueur_actuel.expérience)
                nom.setAttribute("niveau", joueur_actuel.niveau)
                nom.setAttribute("objet_en_main", joueur_actuel.objet_en_main)
                nom.setAttribute("sac", joueur_actuel.sac)
                nom.setAttribute("langage_debloque", joueur_actuel.langage_débloqué)
                nom.setAttribute("vitesse_du_texte", joueur_actuel.vitesse_du_texte)
                nom.setAttribute("dossier_du_jeu", joueur_actuel.dossier_du_jeu)
                nom.setAttribute("fichier_de_sauvegarde", joueur_actuel.fichier_de_sauvegarde)
                fichier_xml_de_sauvegarde.writexml(open(joueur_actuel.dossier_du_jeu  + joueur_actuel.fichier_de_sauvegarde, "w"))
                return None 
        nouveau_joueur = fichier_xml_de_sauvegarde.createElement("joueur")
        nouveau_joueur.appendChild(fichier_xml_de_sauvegarde.createTextNode(joueur_actuel.nom))
        nouveau_joueur.setAttribute("vie", str(joueur_actuel.vie))
        nouveau_joueur.setAttribute("vie_maximal", str(joueur_actuel.vie_maximal))
        nouveau_joueur.setAttribute("argent", str(joueur_actuel.argent))
        nouveau_joueur.setAttribute("argent_banque", str(joueur_actuel.argent_banque))
        nouveau_joueur.setAttribute("experience", str(joueur_actuel.expérience))
        nouveau_joueur.setAttribute("niveau", str(joueur_actuel.niveau))
        nouveau_joueur.setAttribute("objet_en_main", str(joueur_actuel.objet_en_main))
        nouveau_joueur.setAttribute("sac", str(joueur_actuel.sac))
        nouveau_joueur.setAttribute("langage_debloque", str(joueur_actuel.langage_débloqué))
        nouveau_joueur.setAttribute("vitesse_du_texte", str(joueur_actuel.vitesse_du_texte))
        nouveau_joueur.setAttribute("dossier_du_jeu", joueur_actuel.dossier_du_jeu)
        nouveau_joueur.setAttribute("fichier_de_sauvegarde", joueur_actuel.fichier_de_sauvegarde)
        fichier_xml_de_sauvegarde.documentElement.appendChild(nouveau_joueur)
        fichier_xml_de_sauvegarde.writexml(open(joueur_actuel.dossier_du_jeu  + joueur_actuel.fichier_de_sauvegarde, "w"))

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
    jeu.creation_de_la_sauvegarde()
    saut_de_lignes()
    jeu.creation_de_joueur()
    saut_de_lignes()
    scenario()
    saut_de_lignes()
    demande_tutoriel()
    saut_de_lignes()
else:
    jeu.afficher_les_joueurs("\sauvegarde.xml")
    jeu.chargement_du_joueur("\sauvegarde.xml", int(input("Quelle option choisis-tu ? ")))
    village_utilisé.première_fois_village = False
    village_utilisé.première_fois_hopital = False
    village_utilisé.première_fois_banque = False
    village_utilisé.première_fois_shop = False
jeu.sauvegarder()
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