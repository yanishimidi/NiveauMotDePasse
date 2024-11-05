#niveau du mot de passe 
import re
def lvl_mdp(mdp):
    s = 0 
    if len(mdp) >= 8:
        s += 1
    if re.search(r'[A-Z]', mdp):  
        s += 1
    if re.search(r'[a-z]', mdp): 
        s += 1
    if re.search(r'\d', mdp):     
        s += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', mdp):  
        s += 1 

    if s == 5:
        return "Fort"
    elif s >= 3:
        return "Moyen"
    else:
        return "Faible" 
mdp = input("Entrez votre mot de passe : ")
print(lvl_mdp(mdp))



