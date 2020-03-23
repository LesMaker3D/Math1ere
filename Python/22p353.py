def mystere(liste):
        for i in range(len(liste)):
            for j in range(i):
                if liste[j]>liste[j+1]:
                    temp = liste[j]
                    liste[j] = liste[j+1]
                    liste[j+1] = temp
        return liste
            
print(mystere([11,4,3,1,10,4,6,8]))

##Mets la liste dans l'ordre croissant