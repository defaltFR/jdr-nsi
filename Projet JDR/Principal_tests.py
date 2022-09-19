plateau = [["P","-"],["-","-"]]

joueur = [0,0]

n=0


for a in plateau:
    for n in a:
        print(n)
        

gd=("g","d")
hb = ("h", "b")
inp = input("entre h,b,g,d ")

old_pos = []


if inp.lower() in gd:
    if inp.lower() == "d" :
        old_pos = joueur[:]
        joueur[0] -=1
        plateau[joueur[1]][joueur[0]] = "P"
        
        plateau[old_pos[1]][old_pos[0]] = "."
    else:
        old_pos = joueur[:]
        joueur[0] +=1
        plateau[joueur[1]][joueur[0]] = "P"
        
        plateau[old_pos[1]][old_pos[0]] = "."
        
        
elif inp.lower() in hb:
    if inp.lower() == "d" :
        old_pos = joueur[:]
        joueur[1] -=1
        plateau[joueur[1]][joueur[0]] = "P"
        plateau[old_pos[1]][old_pos[0]] = "."
    else:
        old_pos = joueur[:]
        joueur[1] +=1
        plateau[joueur[1]][joueur[0]] = "P"
        plateau[old_pos[1]][old_pos[0]] = "."
else:
    print("non")
        
    
print(plateau, joueur)

    
#     plateau = [["P","B"],["C","D"]]

# joueur = [0,0]

# n=0

# for a in plateau:
#     print(a[n] ,"\n")
#     n+=1

# inp = input("entre h,b,g,d ")
#     :

