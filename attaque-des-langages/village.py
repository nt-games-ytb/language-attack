from colorama import Fore, Style
from playsound import playsound

class Village:
    def __init__(self, première_fois_village, première_fois_hopital, première_fois_banque, première_fois_shop):
        self.première_fois_village = première_fois_village
        self.première_fois_hopital = première_fois_hopital
        self.première_fois_banque = première_fois_banque
        self.première_fois_shop = première_fois_shop
        
    def Texte_de_Mathieu(self):
        print(f"{Fore.RED}M.Mathieu: {Style.RESET_ALL}", end="")
        
    def village(self, joueur):
        self.__hopital(joueur)
        pass
        
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
            print(f"{Fore.MAGENTA}Infirmière Joelle:{Fore.RESET} Bienvue à l'hopital, je suis l'infirmière Joelle est je suis la pour vous soigner !")
        else:
            print("f{Fore.MAGENTA}Infirmière Joelle:{Fore.RESET} Bonjour !")
        print("Voulez-vous être soigné ?\n1 - Oui | 2 - Non")
        réponse_hopital = input()
        if réponse_hopital == "1":
            self.soin(joueur, joueur.vie_maximal)
        elif réponse_hopital == "2":
            print("D'accord, alors j'espère vous revoir bientôt !")
        else:
            print("Désolé mais je n'ai pas compris votre demande...\nJe vous laisse retourner au village, j'espère vous revoir bientôt !")
    
    def soin(self, joueur, point_de_vie):
        joueur.vie = joueur.vie + point_de_vie
        if joueur.vie > joueur.vie_maximal:
            joueur.vie = joueur.vie_maximal
        playsound(joueur.dossier_du_jeu + "\\soin.mp3")
        print("Vous avez êtez soigné de " + str(point_de_vie) + " PV, vous êtes maintenant à " + str(joueur.vie))
    #endregion
        
    #region Banque    
    def __banque(self, joueur):
        if self.première_fois_banque == True:
            print(f"{Fore.YELLOW}Banquier:{Fore.RESET} Bienvue à la banque, je suis votre banquier et c'est moi qui vait gérer votre argent' !")
        else:
            print(f"{Fore.YELLOW}Banquier:{Fore.RESET} Bonjour !")
        print("Que vouslez-vous faire ?\n1 - Déposer de l'argent\n2 - Retirer de l'argent\n3 - Retourner au village")
        réponse_banque = input()
        if réponse_banque == "1":
            self.deposer_argent(joueur, int(input("Combien d'argent voulez-vous déposer ? ")))
        elif réponse_banque == "2":
            self.retirer_argent(joueur, int(input("Combien d'argent voulez-vous retirer ? ")))
        elif réponse_banque == "3":
            print("D'accord, alors j'espère vous revoir bientôt !")
        else:
            print("Désolé mais je n'ai pas compris votre demande...\nJe vous laisse retourner au village, j'espère vous revoir bientôt !")
        
    def __deposer_argent(self, joueur, argent_à_déposer):
        if argent_à_déposer > joueur.argent:
            argent_à_déposer = joueur.argent
        joueur.argent_banque = joueur.argent_banque + argent_à_déposer
        joueur.argent = joueur.argent - argent_à_déposer
        print("Vous avez déposé " + str(argent_à_déposer) + " bitcoin dans votre banque, vous êtes maintenant à " + str(joueur.argent) + " bitcoin avec en plus de cela " + str(joueur.argent_banque) + " bitcoin.")
        
    def __retirer_argent(self, joueur, argent_à_retirer):
        if argent_à_retirer > joueur.argent_banque:
            argent_à_retirer = joueur.argent_banque
        joueur.argent = joueur.argent + argent_à_retirer
        joueur.argent_banque = joueur.argent_banque - argent_à_retirer
        print("Vous avez déposé " + str(argent_à_retirer) + " bitcoin dans votre banque, vous êtes maintenant à " + str(joueur.argent) + " bitcoin avec en plus de cela " + str(joueur.argent_banque) + " bitcoin.")
    #endregion
        
    #region Shop
    def __shop(self, joueur):
        pass
        
    def __afficher_le_shop(self, joueur, items_du_shop):
        pass
        
    def __acheter_au_shop(self, joueur):
        pass
    