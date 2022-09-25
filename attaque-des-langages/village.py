from colorama import Fore, Style
from playsound import playsound
import initialisation

class Village:
    def __init__(self, première_fois_village, première_fois_hopital, première_fois_banque, première_fois_shop):
        self.première_fois_village = première_fois_village
        self.première_fois_hopital = première_fois_hopital
        self.première_fois_banque = première_fois_banque
        self.première_fois_shop = première_fois_shop
        
    def Texte_de_Mathieu(self):
        print(f"{Fore.RED}M.Mathieu: {Style.RESET_ALL}", end="")
        
    def village(self, joueur):
        if self.première_fois_village == True:
            self.Texte_de_Mathieu()
            initialisation.afficher(["Je te présente le village, c'est ici que tu habites.",
            "On y trouve un hopîtal pour se soigner, une banque pour stocker ton argent et un shop pour acheter des armes.",
            "Tu peux aussi partir dans une zone pour aller battre les différents langages."], joueur.vitesse_du_texte, "normal")
            self.première_fois_village = False
        print("Que veux-tu faire ?")
        print("1 - Aller à l'hopîtal")
        print("2 - Aller à la banque")
        print("3 - Aller au shop")
        print("4 - Aller combattre des bugs")
        print("5 - Afficher les caractèristiques")
        #print("6 - Paramètres")
        réponse_village = input()
        initialisation.saut_de_lignes()
        if réponse_village == "1":
            self.__hopital(joueur)
        elif réponse_village == "2":
            self.__banque(joueur)
        elif réponse_village == "3":
            self.__shop(joueur)
        elif réponse_village == "4":
            pass#combat langage
        elif réponse_village == "5":
            joueur.afficher_les_caracteristiques()
        else:
            print("Choix inconnu !")
        
    def decouvert(self):
        lieux_pas_encore_découvert = []
        if self.première_fois_hopital == True:
            lieux_pas_encore_découvert.append("Hopital")
        if self.première_fois_banque == True:
            lieux_pas_encore_découvert.append("Banque")
        if self.première_fois_shop == True:
            lieux_pas_encore_découvert.append("Shop")
        if lieux_pas_encore_découvert != [] :
            print(lieux_pas_encore_découvert)
            print("Vous n'avez pas encore découvert : ", end="")
            for lieux in range(len(lieux_pas_encore_découvert)):
                print(lieux_pas_encore_découvert[lieux] + " ", end="")
        print()
        
    #region Hopital
    def __hopital(self, joueur):
        if self.première_fois_hopital == True:
            print(f"{Fore.MAGENTA}Infirmière Joelle:{Style.RESET_ALL} ", end="")
            initialisation.afficher(["Bienvenue à l'hopital, je suis l'infirmière Joelle et je suis là pour vous soigner !"], joueur.vitesse_du_texte, "normal")
            self.première_fois_hopital = False
        else:
            print(f"{Fore.MAGENTA}Infirmière Joelle:{Style.RESET_ALL} ", end="")
            initialisation.afficher(["Bonjour !"], joueur.vitesse_du_texte, "normal")
        initialisation.afficher(["Voulez-vous être soigné ?"], joueur.vitesse_du_texte, "normal")
        print("1 - Oui | 2 - Non")
        réponse_hopital = input()
        if réponse_hopital == "1":
            self.soin(joueur, joueur.vie_maximal)
        elif réponse_hopital == "2":
            print("D'accord, alors j'espère vous revoir bientôt !")
        else:
            print("Désolé mais je n'ai pas compris votre demande...\nJe vous laisse retourner au village, j'espère vous revoir bientôt !")
        initialisation.saut_de_lignes()
    
    def soin(self, joueur, point_de_vie):
        joueur.vie = joueur.vie + point_de_vie
        if joueur.vie > joueur.vie_maximal:
            joueur.vie = joueur.vie_maximal
        playsound(joueur.dossier_du_jeu + "\\soin.mp3")
        print("Vous avez êtez soigné de " + str(point_de_vie) + " PV, vous êtes maintenant à " + str(joueur.vie) + " PV.")
    #endregion
        
    #region Banque    
    def __banque(self, joueur):
        if self.première_fois_banque == True:
            print(f"{Fore.YELLOW}Banquier:{Style.RESET_ALL} ", end="")
            initialisation.afficher(["Bienvenue à la banque, je suis votre banquier et c'est moi qui vais gérer votre argent !"], joueur.vitesse_du_texte, "normal")
            self.première_fois_banque = False
        else:
            print(f"{Fore.YELLOW}Banquier:{Style.RESET_ALL} ", end="")
            initialisation.afficher(["Bonjour !"], joueur.vitesse_du_texte, "normal")
        initialisation.afficher(["Que voulez-vous faire ?"], joueur.vitesse_du_texte, "normal")
        print("1 - Déposer de l'argent\n2 - Retirer de l'argent\n3 - Retourner au village")
        réponse_banque = input()
        if réponse_banque == "1":
            self.__deposer_argent(joueur, int(input("Combien d'argent voulez-vous déposer ? ")))
        elif réponse_banque == "2":
            self.__retirer_argent(joueur, int(input("Combien d'argent voulez-vous retirer ? ")))
        elif réponse_banque == "3":
            print("D'accord, alors j'espère vous revoir bientôt !")
        else:
            print("Désolé mais je n'ai pas compris votre demande...\nJe vous laisse retourner au village, j'espère vous revoir bientôt !")
        initialisation.saut_de_lignes()
        
    def __deposer_argent(self, joueur, argent_à_déposer):
        if argent_à_déposer > joueur.argent:
            argent_à_déposer = joueur.argent
        joueur.argent_banque = joueur.argent_banque + argent_à_déposer
        joueur.argent = joueur.argent - argent_à_déposer
        playsound(joueur.dossier_du_jeu + "\\banque.mp3")
        print("Vous avez déposé " + str(argent_à_déposer) + " bitcoin dans votre banque, vous êtes maintenant à " + str(joueur.argent) + " bitcoin avec en plus de cela " + str(joueur.argent_banque) + " bitcoin dans votre banque.")
        
    def __retirer_argent(self, joueur, argent_à_retirer):
        if argent_à_retirer > joueur.argent_banque:
            argent_à_retirer = joueur.argent_banque
        joueur.argent = joueur.argent + argent_à_retirer
        joueur.argent_banque = joueur.argent_banque - argent_à_retirer
        playsound(joueur.dossier_du_jeu + "\\banque.mp3")
        print("Vous avez retiré " + str(argent_à_retirer) + " bitcoin dans votre banque, vous êtes maintenant à " + str(joueur.argent) + " bitcoin avec en plus de cela " + str(joueur.argent_banque) + " bitcoin dans votre banque.")
    #endregion
        
    #region Shop
    def __shop(self, joueur):
        pass
        
    def __afficher_le_shop(self, joueur, items_du_shop):
        pass
        
    def __acheter_au_shop(self, joueur):
        pass
    