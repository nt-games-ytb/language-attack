class Joueur:
    def __init__(self, nom, vie, vie_maximal, argent, argent_banque, expérience, niveau, objet_en_main, sac,  langage_débloqué, vitesse_du_texte, dossier_du_jeu, fichier_de_sauvegarde):
        self.nom = nom
        self.vie = vie
        self.vie_maximal = vie_maximal
        self.argent = argent
        self.argent_banque = argent_banque
        self.expérience = expérience
        self.niveau = niveau
        self.objet_en_main = objet_en_main
        self.sac = sac
        self.langage_débloqué = langage_débloqué
        self.vitesse_du_texte = vitesse_du_texte
        self.dossier_du_jeu = dossier_du_jeu
        self.fichier_de_sauvegarde = fichier_de_sauvegarde
        
    def afficher_les_caracteristiques(self):
        print("Voici tes caractèrisitques :")
        print("Nom: " + self.nom)
        print("PV: " + str(self.vie) + "/" + str(self.vie_maximal))
        print("Bitcoin: " + str(self.argent) + " | Bitcoin dans la banque: " + str(self.argent_banque))
        print("Niveau: " + str(self.niveau) + " | Expérience: " + str(self.expérience) + "/" + str(self.niveau * 150))
        print("Vous tenez en main l'objet: " + self.sac[self.objet_en_main])
        print("Votre sac contient: ")
        for objet in self.sac:
            print("- " + objet)
        print("Vous avez débloqué: " + str(self.langage_débloqué) + " langages/30 langages")#Le "s" à langages -> faire un if
        print("Vitesse du jeu: " + str(self.vitesse_du_texte))
        print("Dossier du jeu: " + self.dossier_du_jeu)
        print("Fichier de sauvegarde: " + self.dossier_du_jeu + self.fichier_de_sauvegarde)
        print()