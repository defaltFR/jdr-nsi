class Plateau:
    def __init__(self, x, y, nombre_ditems, nombre_de_monstres):
        self.x = x
        self.y = y
        self.nombre_ditems = nombre_ditems
        self.nombre_de_monstres = nombre_de_monstres
        
    def verification_deplacement(self, plateau, position_du_joueur, future_position):
        
        peut_bouger = False
        
        if future_position.lower() == "g" or future_position.lower() == "d":
            if future_position.lower() == "g":
                if (position_du_joueur[0] - 1) >= 0:
                    peut_bouger = True
                    return peut_bouger
                else:
                    return peut_bouger
                    
            else:
                if ( position_du_joueur[0] + 1) < len(plateau):
                    peut_bouger = True
                    return peut_bouger
                    
            
        elif future_position.lower() == "h" or future_position.lower() == "b":
            if future_position.lower() == "h":
                if (position_du_joueur[1] -1) >= len(plateau):
                    peut_bouger = True
                    return peut_bouger
                else:
                    return peut_bouger
                    
            else:
                if (position_du_joueur[1] + 1) < len(plateau):
                    peut_bouger = True
                    return peut_bouger
                else:
                    return peut_bouger
                
        else:
            print("Veuillez ne saisir que : h, b, g, d")