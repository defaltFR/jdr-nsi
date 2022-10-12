import random
import time
import webbrowser
import sys
import os

class Objet:
    
    def __init__(self, piece, potion ):
        self.piece = piece
        self.potion = potion
        
    def get_piece(self):
        return self.piece

    def get_potion(self):
        return self.potion
    
    def set_piece(self,nvl_piece):
        self.piece = nvl_piece
        
    def set_potion(self,nvl_potion):
        self.potion = nvl_potion
    
    def __repr__(self):
        return f"Le monstre a fait tomber {self.piece} pieces et une potion de {self.potion} PV"
    
class Personnage:
    
    def __init__(self,vie,force,chance,vitesse,nom,piece,potion,objsd=False):
        self.vie=vie
        self.force=force
        self.chance=chance
        self.nom=nom
        self.vitesse=vitesse
        self.piece = piece
        self.potion = potion
        self.objsd = objsd
    def get_vie(self):
        return self.vie
    def get_force(self):
        return self.force
    def get_chance(self):
        return self.chance
    def get_vitesse(self):
        return self.vitesse
    def get_piece(self):
        return self.piece
    def get_potion(self):
        return self.potion
    def get_objsd(self):
        return self.objsd
    def set_vie(self, nouv_vie):
        self.vie = nouv_vie
    def set_force(self, nouv_force):
        self.force = nouv_force
    def set_chance(self, nouv_chance):
        self.chance=nouv_chance
    def set_vitesse(self, nouv_vitesse):
        self.vitesse=nouv_vitesse
    def set_piece(self,nvl_piece):
        self.piece = nvl_piece
    def set_potion(self,nvl_potion):
        self.potion = nvl_potion
    def set_objsd(self,nvl_objsd):
        self.objsd = nvl_objsd
    def __repr__(self):
        return f"{self.nom} a {self.vie} PV, {self.force} de force, {self.vitesse} de vitesse et {self.chance}% de chance, il possede {self.potion} potions et {self.piece} pieces sur lui "
    


def Menu():
    print("                           BIENVENUE SUR RCG6                               ")

    print()
    Menu=""
    liste_c = ["1","2","3"]    
    #Demande du menu de l'utilisateur entre facile, difficile, le reglement et quitter
    print("""Voici les différentes options : 
             
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              -Entre dans le Donjon (Tapez '1')
             
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              -Comment Jouer ? (Tapez '2' 📜 )
            
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              -Quitter (Tapez '3' ❌)
                  
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ """ )
    Menu = input(str("Écrivez votre choix ici : "))
    Menu = Menu.lower()
    #Gestion des cas d'erreurs
    while not (Menu in liste_c):
        print("Erreur❌")
        print("-----------")
        time.sleep(1.5)
        print("""Voici les différentes options : 
             
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              -Entre dans le Donjon (Tapez '1')
             
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              -Comment Jouer ? (Tapez '2' 📜 )
            
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              -Quitter (Tapez '3' ❌)
                  
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ """ )
        Menu = input("Écrivez votre choix ici : ")
        Menu = Menu.lower()
    #En fonction du choix de l'utilisateur, une de ces fonctions se déclenchent
    if Menu== "1":        
        print("\nVous entrez dans le donjon\n")
        time.sleep(1.5)
        donjon()
    elif Menu=="2":
        url = "https://docs.google.com/document/d/1SVkXmDUKV49XNua5USRH1ytIl5LWiliy2WqisZp2KNU/edit"
        webbrowser.open(url)
        revenir_au_menu()
    elif Menu=="3":
            print(sys.exit())

def revenir_au_menu():
    entrée = input("Appuyez sur 'Entrée' pour revenir au menu\n")
    if entrée == "":
        Menu()
    else:
        revenir_au_menu()

def perso_creation():
    
    return per
def game_over():
    print("\nVous etes mort")
    print("\nGAME OVER")
    suivant()
    os.system('cls')
    time.sleep(1.0)
    Menu()

def attaque(adv,per):
    """inflige une attaque  """
    crit=random.randint(1,100) 
    if per.vitesse>adv.vitesse: #si le personnage a plus de vitesse que le monstre
        if crit<per.chance: #si le personnage va infligé un crit
            adv.vie=adv.vie-per.force*1.5
            time.sleep(1)
            print("COUP CRITIQUE !! Vous avez infligé",per.force*1.5,"dégats, il reste",adv.vie ,"à l'adversaire\n")
            time.sleep(1)
            if adv.vie>0: #si le monstre a encore de la vie, il va atk le perso
                if crit<adv.chance:#si le monstre va crit sur le perso
                    per.vie=per.vie-adv.force*1.5
                    print("COUP CRITIQUE !! L'adversaire vous as infligé",adv.force*1.5,"dégats, il vous reste",per.vie,"\n")
                    time.sleep(1)
                    if per.vie<=0:#si le perso na plus de pv
                        time.sleep(1)
                        print("\nVous etes mort")
                        print("GAME OVER")
                        suivant()
                        Menu()
                else:   #si le monstre ne va pas crit sur le perso
                    per.vie=per.vie-adv.force
                    print("L'adversaire vous as infligé",adv.force,"dégats, il vous reste",per.vie)
                    time.sleep(1)
                    if per.vie<=0:#si le perso na plus de pv
                        time.sleep(1)
                        print("\nVous etes mort")
                        print("GAME OVER")
                        suivant()
                        Menu()
            else: #Si le monstre na plus de pv
                time.sleep(1)
                print("\nL'adversaire est mort")
                time.sleep(1)
                rcp(adv, per)
                print("\nLe monstre a fait tomber",adv.piece,"pieces et",adv.potion, "potion\n")
                time.sleep(1)
        else:   #si le perso ne va pas crit
            adv.vie = adv.vie - per.force
            time.sleep(1)
            print("Vous avez infligé",per.force,"dégats, il reste",adv.vie ,"à l'adversaire")
            time.sleep(1)
            if adv.vie>0: #si le monstre a encore des pv
                if crit<adv.chance:#si le monstre va crit sur le perso
                    per.vie=per.vie-adv.force*1.5
                    print("COUP CRITIQUE !! L'adversaire vous as infligé",adv.force*1.5,"dégats, il vous reste",per.vie,"\n")
                    time.sleep(1)
                    if per.vie<=0:#si le perso na plus de pv
                        time.sleep(1)
                        print("\nVous est mort")
                        print("GAME OVER")
                        suivant()
                        Menu()
                else:   #si le monstre ne va pas crit sur le perso
                    per.vie=per.vie-adv.force
                    print("L'adversaire vous as infligé",adv.force,"dégats, il vous reste",per.vie)
                    time.sleep(1)
                    if per.vie<=0:#si le perso na plus de pv
                        time.sleep(1)
                        print("\nVous est mort")
                        print("GAME OVER")
                        suivant()
                        Menu()
            else:
                time.sleep(1)
                print("\nL'adversaire est mort")
                time.sleep(1)
                rcp(adv, per)
                print("\nLe monstre a fait tomber",adv.piece,"pieces et",adv.potion, "potion\n")
                time.sleep(1)
    
    else:   #si le personnage a moins de vitesse que le monstre
        if crit<adv.chance:#si le monstre va crit
            per.vie=per.vie-adv.force*1.5
            print("COUP CRITIQUE !! L'adversaire vous as infligé",adv.force*1.5,"dégats, il vous reste",per.vie,"\n")
            time.sleep(1)
            if per.vie>0:#si le perso a encore des pv
                if crit<per.chance:#si le perso va crit
                    adv.vie=adv.vie-per.force*1.5
                    time.sleep(1)
                    print("COUP CRITIQUE !! Vous avez infligé",per.force*1.5,"dégats, il reste",adv.vie ,"à l'adversaire\n")
                    time.sleep(1)
                    if adv.vie<=0:#si le monstre est mort
                        time.sleep(1)
                        print("\nL'adversaire est mort")
                        time.sleep(1)
                        rcp(adv, per)
                        print("\nLe monstre a fait tomber",adv.piece,"pieces et",adv.potion, "potion\n")
                        time.sleep(1)
                else:   #si le perso ne va pas crit
                    adv.vie=adv.vie-per.force
                    time.sleep(1)
                    print("Vous avez infligé",per.force,"dégats, il reste",adv.vie ,"à l'adversaire")
                    time.sleep(1)
                    if adv.vie<=0:#si le monstre est mort
                        time.sleep(1)
                        print("\nL'adversaire est mort")
                        time.sleep(1)
                        rcp(adv, per)
                        print("\nLe monstre a fait tomber",adv.piece,"pieces et",adv.potion, "potion\n")
                        time.sleep(1)
            else:#si le perso na plus de pv
                print("\nVous est mort")
                print("GAME OVER")
                suivant()
                Menu()
        else:   #si le monstre ne va pas crit
            per.vie = per.vie - adv.force
            time.sleep(1)
            print("L'adversaire vous as infligé",adv.force,"dégats, il vous reste",per.vie)
            time.sleep(1)
            if per.vie>0:#si le perso a encore de la vie
                adv.vie=adv.vie-per.force
                print("Vous avez infligé",per.force,"dégats, il reste",adv.vie ,"à l'adversaire")
                if adv.vie<=0:#si le monstre na plus de vie
                    time.sleep(1)
                    print("\nL'adversaire est mort")
                    time.sleep(1)
                    rcp(adv, per)
                    print("\nLe monstre a fait tomber",adv.piece,"pieces et",adv.potion, "potion\n")
                    time.sleep(1)
                    
            else:#si le perso n'a plus de vie
                print("\nVous êtes mort")
                print("GAME OVER")
                suivant()
                Menu()
def combat(adv,per):
    print(adv,"\n")
    print(per,"\n")
    
    while adv.vie>0 and per.vie>0:
        if per.vie - adv.force<=0:
            choix=input("\nVous n'avez plus beaucoup de PV, voulez vous fuir ? (Oui ou Non) ")
            if choix.lower()== "oui":
                fuite=random.randint(1,100)
                if fuite<per.chance:
                    print("Vous avez réussi à fuir le combat")
                else:
                    print("Vous n'avez pas réussi à fuir, vous aviez",per.chance,"% de chance de fuir")
                    per.vie = per.vie - adv.force
                    print("L'adversaire vous as infligé",adv.force,"dégats, il vous reste",per.vie)
                    time.sleep(2)
                    print("Vous êtes mort.")
                    print("GAME OVER")
                    suivant()
                    Menu()
            else:
                attaque(adv,per)
               
        else:
            attaque(adv,per)
            
    return("cequecocrentinfait")

def rcp(adv,per):
    per.piece = per.piece + adv.piece
    per.potion = per.potion + adv.potion
    
           
def choix_salle():
 
    salle=random.randint(1,100)
    print(salle)
    if salle<41:
        adv=Personnage(10,5,random.randint(1,50),100,plouk[random.randint(0,11)],random.randint(1,2),0)
        combat(adv,per)
    elif 40<salle<61:
        adv=Personnage(20,10,random.randint(1,50),50,loubard[random.randint(0,9)],random.randint(1,5),random.randint(0,1))
        combat(adv,per)
    elif 60<salle<71:
        adv=Personnage(50,25,random.randint(1,50),10,scelerat[random.randint(0,7)],random.randint(5,15),random.randint(1,2))
        combat(adv,per)
    elif 70<salle<76:
        adv=Personnage(15,35,random.randint(25,75),25,alchimiste[random.randint(0,6)],random.randint(15,25),2)
        combat(adv,per)
    elif 75<salle<77:
        adv=Personnage(1000000,100000,1000000,100,"Thérentek",500,15)
        combat(adv,per)
    elif 76<salle<82:
        coffre()
    elif 81<salle<92:
        print("evenement aléatoire")
    else:
        print("salle vide")

def suivant():
    input("Appuyez sur 'Entrée' pour continuer\n")       
    
plouk = ["Gerbantin Le Plouk Malicieux","Garry Le Plouk Hardy","Tanguy Le Plouk Chenapan","Eric Le Plouk Sadique","Bertrand Le Plouk Plouc","Mario Le Plouk Plombier","Aymeric Le Plouk Ecorcheur","Douceur Le Plouk Farceur","Gertrude La Ploukette Canaille","Karine La Ploukette Marchande","Viviane La Ploukette Fripouille","Bernadette La Ploukette Simplette"]

loubard =["Charlie Le Loubard", "Tango Le Loubard", "Foxtrot Le Loubard", "Echo Le Loubard", "Delta Le Loubard", "Zulu Le Loubard", "Mike Le Loubard", "Walter Le Loubard", "Juliette La Loubarde", "Oscar Le Loubard"]

scelerat = ["Arsène Le Scélérat", "Redouane Le Scélérat", "Michael Le Scélérat", "Fernando Le Scélérat", "Sara La Scélérate", "Skyler La Scélérate", "Gustavo Le Scélérat","Pablo Le Scélérat"]
    
alchimiste =["Ey-Lium L'Alchimiste","Chrome L'Alchimiste","A-Zot L'Alchimiste","Soy-Diom L'Alchimiste","Nick-El L'Alchimiste","Maître Iode L'Alchimiste","Françis Ium L'Alchimiste"]     

def coffre():
    choix_coffre = input("Vous tombez sur un coffre enfoui dans le sol... Voulez voulez vous l'ouvrir ? (Tapez Oui ou Non)")
    obj=random.randint(1,100)
    if choix_coffre.lower() == "oui":
        if obj<=20:
            per.force = per.force + 10
            print("Vous avez trouvez une épée ! Elle vous octroie 10 de Force en plus")
        elif 20<obj<41:
            per.vitesse = per.vitesse + 10
            print("Vous avez trouvé des Adidas™ SpeedFlow XZ ! Vous gagnez 10 de vitesse en plus ")
        elif 40<obj<71:
            random_piece = random.randint(20,40)
            per.piece = per.piece + random_piece
            print("Vous avez trouvé ", random_piece,  " pieces ! Elles s'ajoutent au pieces déjà présente dans votre morlingue")
        elif 70<obj<81:
            print("Vous ouvrez le coffre et vous y trouvez...")
            suivant()
            print("UN PLOUK CACHÉ DANS LE COFFRE ! il vous saute dessus et vous attaque !!")
            adv=Personnage(10,5,random.randint(1,50),100,plouk[random.randint(0,11)],random.randint(1,2),0)
            combat(adv,per)
        elif 80<obj<88:
            per.vie = per.vie - 20
            print("BOOM 💥💥 !! Vous êtes tombé sur un coffre piegé... Vous avez perdu 20 PV")
        elif 87<obj<99:
            print("Ce coffre est vide !")
        else:
            print("VOUS AVEZ TROUVE LA SUPER GIGA SUPRA EPEE MAGIQUE CALECHISEE")
            per.objsd = True
        

Menu()
perso_nom=input("Choississez le nom de votre aventurier : \n")
per=Personnage(random.randint(1,100),random.randint(10,100),random.randint(1,100),random.randint(1,100),perso_nom,0,0)



class Map:
    def __init__(self, taille_plateau, nombre_ditems, nombre_de_monstres, joueur):
        self.nombre_ditems = nombre_ditems
        self.nombre_de_monstres = nombre_de_monstres
        self.joueur = joueur
        self.taille_plateau = taille_plateau
        
      
    def afficher_plateau(self, plateau):
        for ligne in plateau:
            chaine = ""
            for c in ligne:
                chaine += c
            
            print(chaine)

    
    def verification_deplacement(self, plateau, future_position):
        
        peut_bouger = False
        
        if future_position.lower() == "g" or future_position.lower() == "d":
            if future_position.lower() == "g":
                if (self.joueur[0] - 1) >= 0:
                    peut_bouger = True
                    return peut_bouger
                else:
                    return peut_bouger
                    
            else:
                if ( self.joueur[0] + 1) < len(plateau[0]):
                    peut_bouger = True
                    return peut_bouger
                    
            
        elif future_position.lower() == "h" or future_position.lower() == "b":
            if future_position.lower() == "h":
                if (self.joueur[1]  -1) >= 0 :
                    peut_bouger = True
                    return peut_bouger
                else:
                    print("cant")
                    return peut_bouger
                    
                    
            else:
                if (self.joueur[1] + 1) < len(plateau):
                    peut_bouger = True
                    return peut_bouger
                else:
                    return peut_bouger
                
        else:
            print("Veuillez ne saisir que : h, b, g, d")
            
    def deplacement(self, inp, plateau):
        gd=("g","d")
        hb = ("h", "b")
        old_pos = []
        if inp.lower() in gd:
            if inp.lower() == "g" :
                if (self.verification_deplacement(plateau, inp) == True):
                    old_pos = self.joueur[:]
                    self.joueur[0] -=1
                    plateau[self.joueur[1]][self.joueur[0]] = "P "
                    plateau[old_pos[1]][old_pos[0]] = "º  "
            else:
                if (self.verification_deplacement(plateau, inp) == True):
                    choix_salle()
                    old_pos = self.joueur[:]
                    self.joueur[0] +=1
                    plateau[self.joueur[1]][self.joueur[0]] = "P "
                    plateau[old_pos[1]][old_pos[0]] = "º "
                
                
        elif inp.lower() in hb:
            if inp.lower() == "h" :
                if (self.verification_deplacement(plateau, inp) == True):
                    old_pos = self.joueur[:]
                    self.joueur[1] -=1
                    plateau[self.joueur[1]][self.joueur[0]] = "P "
                    plateau[old_pos[1]][old_pos[0]] = "º "
            else:
                if (self.verification_deplacement(plateau, inp) == True):
                    old_pos = self.joueur[:]
                    self.joueur[1] +=1
                    plateau[self.joueur[1]][self.joueur[0]] = "P "
                    plateau[old_pos[1]][old_pos[0]] = "º "
        else:
            print("Veuillez n'entrer que h,b,g et d")

    def plat(self):
        
        
        p=[]
        for col in range(0, self.taille_plateau):
            lignes =[]
            for li in range(0, self.taille_plateau):
            
                lignes.append("• ")
            p.append(lignes) 
        p[self.joueur[1]][self.joueur[0]] ="P "
        
        
        
        return p
    

        

# position = [0,0]


# plateau1 = Map(20, 4, 6, position)

# jouer = True

# carte = plateau1.plat() 


# while jouer:  
    
#     plateau1.afficher_plateau(carte)

#     depla = input(f"haut(h)↑ bas(b)↓ gauche(g)← droite(d)→ [{per.potion}]potion(p)🍼 : ")
    
#     if depla.lower() == "p":
#         if per.potion > 0 :
#             per.potion -= 1
#             per.vie += 10
#             print("vous gagnez 10pv en plus")
#             suivant()
#         else:
#             print("Vous n'avez plus de potions")
#             suivant()
#     else:
#         plateau1.deplacement(depla, carte)
#         suivant()
    

def initialisation_jeu():
    position = [0,0]

    plateau1 = Map(20, 4, 6, position)

    jouer = True

    carte = plateau1.plat() 
    
    perso_nom=input("Choississez le nom de votre aventurier : \n")
    per=Personnage(random.randint(1,100),random.randint(10,100),random.randint(1,100),random.randint(1,100),perso_nom,0,0)
    plateau1.afficher_plateau(carte)
    while jouer==True:
        depla = input(f"haut(h)↑ bas(b)↓ gauche(g)← droite(d)→ [{per.potion}]potion(p)🍼 : ")
        
        if depla.lower() == "p":
            if per.potion > 0 :
                per.potion -= 1
                per.vie += 10
                print("vous gagnez 10pv en plus")
                suivant()
            else:
                print("Vous n'avez plus de potions")
                suivant()
        else:
            plateau1.deplacement(depla, carte)
            time.sleep(1.0) 
        return per
    
    
    

    

    

