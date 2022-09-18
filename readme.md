# Projet de NSI n°1 - TORO Nicolas TG09 :
# L'attaque des langages

## Consignes
- Créer un programme Python faisant intervenir les classes
- Groupe de 1 ou 2 élèves
- Le reste du projet est libre

## But du pojet
Créer un jeu en python utilisant différentes classes. Ce jeu est un RPG consistant à vaincre les bugs (ou zombies) des différents langages de programmation classés du plus récent au plus ancien pour à la fin les réparer.

## Scènario
Grâce aux cours de M.Duranton et de M.Maurice, les élèves de terminal du lycée Thierry Maulnier apprennent le python mais bien sur cela ne se passe pas comme prévu. Certains élèves sont perdus, d'autres n'écoutent pas ou utilisent leur téléphone portable et même certains ont mis 2 semaines pour arriver en cours... Heureusement, vous, vous arrivez à remonter le niveau de cette classe désastreuse. C'est alors qu'un beau jour, à force d'une utilisation déplorable de Python avec EduPython qui crashait toutes les 2 minutes, qu'une faille se créa. Cette faille permit l'entrer à de nombreux bugs dans les différents langages de programmation existants. Etant le seul capable de faire un script python dans votre classe, vous allez essayer de faire disparaitre et de supprimer ces bugs. Cela ne va pas être si simple mais M.Mathieu (ancien professeur de NSI au lycée Thierry Maulnier) sera là pour vous épauler et pour aider à détruire ces bugs. Alors, pourrez-vous exterminer tous ces bugs et ainsi réparer les divers langages de programmation ? 

## Objectifs
*Les commentaires sont en italic*    
*Les mots en gras représentent des noms de fonctions ou de variables*
*Les mots et phrases barré sont les choses abandonnées (soit parce que ce n'est pas possible avec le materiel du lycée ou soit pour d'autres raisons)*

### Général :
- [ ] Faire que le jeu soit joueable
- [ ] Utiliser **Colorama**. Comme les ordinnateurs du lycée ne sont pas perfommant, possèdent peu de librairy pré-installé et comme on ne peut pas en installer d'autres, alors j'ai choisis d'utiliser **Colorama**. C'est l'une des plus populaire et elle fonctionne parfaitement avec les ordinateurs du lycée.
- [ ] Lors du lancement du jeu si le fichier "sauvegarde.xml" existe lancer la fonction **afficher_les_joueurs** sinon lancer la fonction **creation_de_la_sauvegarde**.

#### Initialisation et XML :
- [ ] Faire une fonction privée nommé **"creation_de_joueur"** qui créera un fichier nommé "sauvegarde.xml" (dans le dossier "attaque-des-langages") et qui contiendra les bases
- [ ] Faire une fonction privée nommé **"creation_de_joueur"** qui demandera un nom de joueur, qui créera **"joueur_actuel"** avec la classe **joueur** et qui sauvegardera ce joueur dans le fichier "sauvegarde.xml". Si le nom choisis existe déjà alors demander un autre nom jusqu'à ce l'utilisateur trouve un nom qui n'existe pas dans le fichier.
- [ ] Faire une fonction privée nommé **"afficher_les_joueurs"** qui lira les joueurs sauvegardé dans le fichier "sauvegarde.xml" et qui les affichera un par un (avec une numérotation).
- [ ] Faire qu'après avoir afficher les joueurs (grâce à la fonction **afficher_les_joueurs**), le script nous demande le numéro du joueur et lancera ensuite **chargement_du_joueur**.
- [ ] Faire une fonction privée nommé **"chargement_du_joueur"** qui prend comme paramètre **"numéro_du_joueur"** (un integer), qui lira données du joueur choisis (grâce au **numéro_du_joueur**) et qui avec, créera **"joueur_actuel"** avec la classe **joueur**.
- [ ] Faire une fonction public nommé **"sauvegarder"** qui prend comme paramètre **"joueur"** (un integer), soit le **joueur_actuel** au quelle ses données seront sauvegarder dans le fichier "sauvegarde.xml". Elle sera utilisé souvent pour ne pas avoir de problème si le jeu plante où si un problème apparait.

### Village :
- [ ] Quand on est dans le villages, on doit avoir un menu qui nous demande ce qu'on veut faire, soit :    
Parler à M.Mathieu (si l'option est choisis alors M.Mathieu vous redira les dernières choses qu'il vous as précédement dite)    
Aller à l'hopîtal (si l'option est choisis alors lance la fonction **hopital**)    
Aller à la banque (si l'option est choisis alors lance la fonction **banque**)
Aller au shop (si l'option est choisis alors lance la fonction **shop**)


#### Hopital :
- [ ] Faire une fonction privée nommé **"soin"** qui prend comme paramètre **"vie"** (un integer), soit la vie qui sera ajoutée à vos **point_de_vie**. Si votre vie dépasse ensuite votre **vie_maximale** alors votre vie sera égale à votre **vie_maximale**.    
- [ ] Faire une fonction privée nommé **"hopital"** qui vous demandera si vous êtes sur de vouloir vous soigner, si oui alors lancer la fonction **soin** avec comme paramètre la **vie_maximale** sinon retour au village.    

#### Banque :
- [ ] Faire une fonction privée nommé **"déposer_argent"** qui prend comme paramètre **"argent"** (un integer), soit l'argent que le script prendra de l'argument **argent**"** pour le mettre dans l'argument **argentSauvegardé**. Si le nombre est trop grand alors le jeu doit informer le joueur.    
- [ ] Faire une fonction privée nommé **"retirer_argent"** qui prend comme paramètre **"argent"** (un integer), soit l'argent que le script prendra de l'argument **argentSauvegardé** pour le mettre dans l'argument **argent**. Si le nombre est trop grand alors le jeu doit informer le joueur.    
- [ ] Ajouter un son spéciales pour ces deux fonctions.    
- [ ] Faire une fonction privée nommé **"banque"** qui vous demandera ce vous voulez faire à la banque, selon le choix le script lancera les fonctions **déposer_argent**, **retirer_argent** ou retounera au village.    

#### Shop : 
- [ ] Faire une fonction privée nommé **"afficher_le_shop"** qui prend comme paramètre **"items_du_shop"** (une liste qui contient une liste pour chaque items) avec laquelle il va afficher chaque items du shop ainsi que ses caractèristiques *(Pour plus tard : mettre du couleur spéciale pour les items déjà changer)*.
- [ ] Faire une fonction privée nommé **"acheter_au_shop"** qui prend comme paramètre **"numéro_items"** (un integer), soit le numéro de l'items qu'il va d'abords regarder si tu le joueur le possède et si il le possède pas alors il va regarder si le joueur à assez d'argent, si il en a assez alors à ce moment là, le jeu va mettre le nouvelle item dans le **sac**. Emettre un son lorsque l'achat est effectué. *(Pour plus tard : si c'est une arme alors demander si le joueur veut prendre en main l'items)*
- [ ] Faire une fonction privée nommé **"shop"** qui lancera directement **afficher_le_shop**, puis, qui vous demandera ce vous voulez faire au shop, selon le choix le script lancera **acheter_au_shop** (avec le **numéro_items** demandé) ou retournera au village.   

### Pour plus tard
- [ ] ~~Adapter certaines fonctions qui demande demande des chiffres pour exercer certaines actions en button avec **Curses** (voir [exemple](https://www.youtube.com/watch?v=Db4oc8qc9RU)).~~
  

## Difficultées rencontrer