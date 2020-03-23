from math import *

def div(n,l):
    compteur = 0
    for i in range(len(l)):
        if (l[i]%n == 0):
            compteur = compteur+1
    if compteur == len(l):
        return True
    else:
        return False


def div_commun(l):
    l.sort()
    diviseur = []
    for i in range(1, l[len(l)-1]):
        if div(i,l) == True:
            temp = i
            diviseur.append(temp)
    return(diviseur)



l = [420, 294, 343]
print(div_commun(l))

##Max 7mm
##294/7 =42
## 420/7 = 60
#343/7 = 49
# 42*60*49 = 123480 cubes