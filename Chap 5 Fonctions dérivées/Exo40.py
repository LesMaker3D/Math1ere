a = eval(input("Entrez la valeur a "))
b = eval(input("Entrez la valeur b "))
c = eval(input("Entrez la valeur c "))



def fu(a,b,c):
    v = -b/2*a
    if a > 0:
        print("F est décroissante sur l'intervalle ]-Infini;", v, "]")
        print("F est croissante sur l'intervalle ]", v, "; +Infini [")
    elif a < 0:
        print("F est croissante sur l'intervalle ]-Infini;", v, "]")
        print("F est décroissante sur l'intervalle ]", v, "; +Infini [")
    else:
        print("F n'est pas un polynôme du second degré.")


fu(a,b,c)