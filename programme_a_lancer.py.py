# coding: utf-8

import sys
import os
import dico
import liste_fonction


i=0
repertoire='%s\sauvegardes'%os.getcwd()

while i!=1:
    action=str(input("Que voulez vous faire? \n \
Taper 'H' pour voir les différentes commandes. \n \
Commandes?= ")).lower()
    
    if action=='q':
        i=1
        
    elif action=='a':
        A=liste_fonction.apprendre(repertoire)
        i=0
        print("\n")
        
    elif action=='h':
        print("\n\n Taper:\n \
H pour aide.                E pour effacer toutes mes données \n \
Q pour quitter              L pour afficher les mots que je connais\n \
A pour me faire apprendre.  D pour que je vous donne une définition \n\n")
              
    elif action=='l':
        liste_fonction.affichage_liste_mots_connus(repertoire)
        i=0

    elif action=='e':
        liste_fonction.effacement_donnees(repertoire)
        i=0
    elif action=='d':
        liste_fonction.definition_mot(repertoire)
        i=0
    elif action=='ct':
        liste_fonction.controle(repertoire)
        i=0
                
    else:
        print("Commande invalide. Taper H pour consulter les commandes.")
        i=0
        
print("\n\n Merci pour cette leçon. \n \
Aurevoir et à bientôt.")

os.system("pause")
