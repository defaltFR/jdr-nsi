# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:43:46 2022

@author: CLOUIS
"""

plateau = [["P","-","-"],["-","-","-"]]

for ligne in plateau:
    chaine = ""
    for c in ligne:
        
        chaine += c
        
    print(chaine)
    
    
    
def afficher_plateau(plateau):
    for ligne in plateau:
        chaine = ""
        for c in ligne:
            chaine += c
        
        print(chaine)