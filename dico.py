# coding: utf-8

import pickle
import dico


class Dico():
    """ Classe définissant les mots appris par le programme"""
    def __init__(self,nom):
        self.nom= nom
        self.donnees={}


    def implement(self,mot,valeur=1):
        """ Augmente ou diminue la valeur de vérité d'une définition \
relativement à un mot."""
        if mot in self.donnees:
            self.donnees[mot]+=valeur
        else:
            self.donnees[mot]=valeur


    def enregistrer(self, repertoire):
        """ Crée un nouveau fichier mots ou mets à jour les anciens d'aprés les données en cours. """
        
        with open('%s//liste_de_mots.txt'%repertoire,'rb') as fichier:
            mots_connus=pickle.Unpickler(fichier)
            liste_mots_connus=mots_connus.load()
                        
            if self.nom in liste_mots_connus:
                self.sauvegarde(repertoire)

            else:
                liste_mots_connus+=[self.nom]
                
                with open('%s//liste_de_mots.txt'%repertoire,'wb') as fichier:
                    x=pickle.Pickler(fichier)
                    x.dump(liste_mots_connus)
                   
                with open('{0}//{1}.txt'.format(repertoire, self.nom),'wb') as fichier:
                    x=pickle.Pickler(fichier)
                    x.dump(self.donnees)
        return liste_mots_connus
                

    def sauvegarde(self, repertoire):
        """ Fonction de ENREGISTRER qui enregistre l'apprentissage relatif au mot en cours \
et la stocke dans un fichier portant le nom du mot. \n
Uniquement si le fichier existe déjà."""
        
        with open('{0}//{1}.txt'.format(repertoire, self.nom),'rb') as fichier:
            x=pickle.Unpickler(fichier)
            x=x.load()
            
        for key, value in x.items():
            self.implement(str(key), int(value))
           
        with open('{0}//{1}.txt'.format(repertoire, self.nom),'wb') as fichier:
            x=pickle.Pickler(fichier)
            x.dump(self.donnees)
            
            
         
                    
        
if __name__=="__main__":
    
    import os
    repertoire='%s\sauvegardes'%os.getcwd()          

    A=Dico("table")
    A.implement("meuble",2)
    A.implement("meuble",1)
    A.implement("miel",-1)
    print("Le contenue de A sur ce tour est",A.donnees)
    A.enregistrer(repertoire)

    with open('%s//liste_de_mots.txt'%repertoire,'rb') as fichier:
        mots_connus=pickle.Unpickler(fichier)
        lists=mots_connus.load()
        print(lists)

    with open('%s//table.txt'%repertoire,'rb') as fichier:
        mots_connus=pickle.Unpickler(fichier)
        lists=mots_connus.load()
        print(lists, len(lists))
    
