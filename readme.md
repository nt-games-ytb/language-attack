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
*Les mots en gras représentent des noms de fonctions ou de variables*

### Village :
- [ ] Quand on est dans le villages, on doit avoir un menu qui nous demande ce qu'on veut faire, soit :    
Parler à M.Mathieu (si l'option est choisis alors M.Mathieu vous redira les dernières choses qu'il vous as précédement dite)    
Aller à l'hopîtal (si l'option est choisis alors la fonction **hopital**)    
Aller à la banque ()

    #### Hopital :
    - [ ] Faire une fonction privée nommé **"soin"** qui prend qui prend comme paramètre **"vie"**, soit la vie qui sera ajoutée à vos **point_de_vie**. Si votre vie dépasse ensuite votre **vie_maximale** alors votre vie sera égale à votre **vie_maximale**.    
    - [ ] Faire une fonction privée nommé **"hopital"** qui vous demandera si vous êtes sur de vouloir vous soigner, si oui alors lancer la fonction **soin** avec comme paramètre la **vie_maximale**.    

#### Banque :
- [ ] Faire une fonction privée nommé **"déposer_argent"** qui prend comme paramètre **"argent"** (un integer), soit l'argent que le script prendra de l'argument **argent**"** pour le mettre dans l'argument **argentSauvegardé**. Si le nombre est trop grand alors le jeu doit informer le joueur.    
- [ ] Faire une fonction privée nommé **"retirer_argent"** qui prend comme paramètre **"argent"** (un integer), soit l'argent que le script prendra de l'argument **argentSauvegardé** pour le mettre dans l'argument **argent**. Si le nombre est trop grand alors le jeu doit informer le joueur.    
- [ ] Ajouter un son spéciales pour ces deux fonctions.    
- [ ] Faire une fonction privée nommé **"banque"** qui vous demandera si ce vous voulez faire à la banque, selon le choix le script lance les fonctions **déposer_argent** ou **retirer_argent** (ou retour au village si demandé).    

#### Shop : 



## Difficultées rencontrer
