# coding: utf-8

""" Liste de fonctions pour le fichier programme"""
import os
from operator import itemgetter, attrgetter
import pickle
import dico
import fonctions_secondaires


def apprendre(repertoire):
    """ Demande un mot et sa définition puis stocke l'ensemble dans le dossier \
sauvegarde. """
    
    mot=input("\n\n Quel mot souhaitez vous me faire apprendre?=").lower()
    definition=input("\nComment définiriez vous ce mot? \n\
(Tapez: 'mot' ou 'mot, mot,...' ou 'mot_compose')  \n Definition=" ).lower()
   
    definition=definition.replace(',','').split()
    objet=dico.Dico(mot)
    
    for variable in definition:
        objet.implement(variable)

    objet.enregistrer(repertoire)
    return objet


def affichage_liste_mots_connus(repertoire):
    """ Affiche l'ensemble des mots contenus dans le fichier liste_mots_connus \
du dossier sauvegarde."""
    
    with open('%s//liste_de_mots.txt'%repertoire,'rb') as fichier:
            mots_connus=pickle.Unpickler(fichier)
            liste_mots_connus=mots_connus.load()
            print("\n\n Je connais les mots suivants: \n", \
liste_mots_connus,"\n\n")

    
def effacement_donnees(repertoire):
    """ Efface tous les fichiers du dossier sauvegarde et recréé un \
fichier liste_de_mots vierge."""
    
    liste_fichiers=os.listdir(repertoire)
    for fichier in liste_fichiers:
        os.remove('{0}//{1}'.format(repertoire,fichier))
        with open('%s//liste_de_mots.txt'%repertoire,'wb') as fichier:
            x=pickle.Pickler(fichier)
            nouvelle_liste=[]
            x.dump(nouvelle_liste)
    print("\n\n Ma mémoire a été effacée.\n\n ")

def controle(repertoire):
    x=input("Quel mot à contrôler=")
    with open('{0}//{1}.txt'.format(repertoire, x),'rb') as fichier:
            x=pickle.Unpickler(fichier)
            x=x.load()
            print(x)
            print(len(x))
            

def definition_mot(repertoire):
    """ Demande un mot et affiche la ou les meilleure(s) définition(s) que le progamme\
ait appris de ce mot. """
    
    mot=input("\n\n Quel mot chercher vous à définir?= ").lower()
    with open('%s//liste_de_mots.txt'%repertoire,'rb') as fichier:
            mots_connus=pickle.Unpickler(fichier)
            liste_mots_connus=mots_connus.load()

    if mot in liste_mots_connus:
        with open('{0}//{1}.txt'.format(repertoire,mot),'rb') as fichier:
            mot_identifie=pickle.Unpickler(fichier)
            objet_mot=mot_identifie.load()

        definition=[]
        for attribut, valeur in objet_mot.items():
            definition.append((attribut,valeur))    
        definition=fonctions_secondaires.best_definition(definition)
        definition=' ou '.join(definition)
        print("\n\n La meilleur définition de",mot, \
"est selon moi:", definition,".\n\n")

    else:
        print("\n\n Le mot ",mot,"ne fait pas partie de mon vocabulaire. Désolé. \n\n")
        




if __name__=="__main__":
    repertoire='%s\sauvegardes'%os.getcwd()
    apprendre(repertoire)
