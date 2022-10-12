# EXO 3 La afficher la mention d'un élève
note1 = int(input("Enter votre prémière note: "))
note2 = int(input("Enter votre deuxième note: "))
note3 = int(input("Enter votre troisième note: "))
mark = (note1+note2+note3)/3
if mark >= 16:
    print(f"Bravo vous etes admis avec une mention Très bien avec une moyenne de {mark}")
elif mark >= 14 and mark < 16:
    print(f"bravo vous etes admis avec une mention Bien avec une moyenne de {mark} ")
elif mark >= 12 and mark < 14:
    print(f"félicitation vous etes admis avec la mention Assez-bien avec une moyenne de {mark}")
elif mark >= 10 and mark < 12:
    print(f"pas de mal vous etes admis avec une mention Passable avec une moyenne de {mark}")
else:
    print(f"désolé votre moyenne est insuffisante avec une moyenne de {mark}")