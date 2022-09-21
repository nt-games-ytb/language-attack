    def afficher_les_joueurs(self, fichier):
        print("Un fichier de sauvegarde a été trouvé !")
        print("Plusieurs options s'offre donc à toi, elle sont les suivantes :")
        print("0 - Créer un nouveau joueur")
        fichier_xml_de_sauvegarde = xml.dom.minidom.parse(self.dossier + fichier)
        liste_des_joueurs = fichier_xml_de_sauvegarde.documentElement.getElementsByTagName("joueur")
        numéro_joueur = 1
        for nom in liste_des_joueurs:
            print(str(numéro_joueur) + " - Jouer avec " + nom.getAttribute("nom"))
            numéro_joueur = numéro_joueur + 1
        if numéro_joueur == 1:
            print(f"{Fore.RED}Malheuresement, nous n'avons pas réussi à charger de joueurs.{Fore.RESET}")

    def chargement_du_joueur(self, fichier, numéro_du_joueur):
        if numéro_du_joueur == 0:
            self.creation_de_joueur()
        else:
            fichier_xml_de_sauvegarde = xml.dom.minidom.parse(self.dossier + fichier)
            liste_des_joueurs = fichier_xml_de_sauvegarde.documentElement.getElementsByTagName("joueur")
            joueur_actuel.nom = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("nom")
            joueur_actuel.vie = liste_des_joueurs[numéro_du_joueur - 1].getElementsByTagName("vie")[0].childNodes[0].nodeValue
            '''joueur_actuel.vie_maximal = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("vie_maximal")
            joueur_actuel.argent = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("argent")
            joueur_actuel.argent_banque = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("argent_banque")
            joueur_actuel.expérience = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("experience")
            joueur_actuel.niveau = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("niveau")
            joueur_actuel.objet_en_main = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("objet_en_main")
            joueur_actuel.sac = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("sac")
            joueur_actuel.langage_débloqué = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("langage_debloque")
            joueur_actuel.vitesse_du_texte = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("vitesse_du_texte")
            joueur_actuel.dossier_du_jeu = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("dossier_du_jeu")
            joueur_actuel.fichier_de_sauvegarde = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("fichier_de_sauvegarde")'''

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