# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:27:20 2021

@author: ACER
"""
def jeu():
    
    import random
    mots=[]
    
    with open("lesMots.txt") as fl :
        for l in fl:
            mots.append(l.rstrip("\n"))
    mot=random.choice(mots)
    
    lettres=[]
    faux = 0
    trouve=False
    corps_plein=["o","/","|","\\","/","\\"]
    corps=[" "," "," "," "," "," "]
    
    
    
    
    while not trouve:
        trouve=True
        print(" +---+")
        print(" |   |")
        print(" |   {}".format(corps[0]))
        print(" |  {}{}{}".format(corps[1],corps[2],corps[3]))
        print(" |  {} {}".format(corps[4],corps[5]))
        print("_|_")
        print("| |")
         
        for l in mot:
            if l in lettres:
                print(l,end=" ")
            else:
                trouve=False
                print("_",end=" ")
                
        if faux > 5:
            print("Tu as perdu !")
            choix1=input("{} voulez vous réessayer(o/n) : ".format(nom))
            if choix1=='o':
                jeu()
            else:
                break
            
            
        
        if trouve:
            print("Tu a gagné !")
            choix2=input("{} voulez vous réessayer(o/n) : ".format(nom))
            if choix2=='o':
                jeu()
            else:
                break
            
        
        lettre=input("Entrez une lettre: ")
        lettres.append(lettre)
        
        if lettre not in mot:
            corps[faux]=corps_plein[faux]
            faux += 1
print("   ++++++ Jeu du pendu ++++++")
nom =input("Entrer votre nom : ")
print("{} Bienvenue  dans le jeu du pendu.\nLe jeu consiste à deviner un mot cacher.".format(nom))
print("vous allez entrer une lettre à chaque fois.")
jeu()
        
        
        


    