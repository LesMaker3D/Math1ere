a= float(input("Donné a"))
b= float(input("Donné b"))
c= float(input("Donné c"))

delta=b*b-4*a*c
print(delta)

if delta < 0:
    print("Aucune solutions disponibles")
if delta==0:
    resultat3=(-b/(2*a))
    print("Le resulat est", resultat3)
if delta > 0:
    resultat=(-b-(delta/delta)/(2*a))
    resultat1=(-b+(delta/delta)/(2*a))
    print("Le premier résultat est",resultat)
    print("Le deuxieme résultat est",resultat1)
