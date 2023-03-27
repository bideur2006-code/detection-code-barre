from math import *
import time
# demande des 15 chiffre de la carte bancaire
# ---------------------------------------
repeat = 0
while repeat == 0:
    CB_number = []
    for HDU_boucle in range (1,13):
        verif = input("entré le chffre n°" + str(HDU_boucle) + " de votre code barre\n")
        try:
            CB_number.append(int(verif))
            repeat = 1
        except:
            print("Erreur : veuillez mettre un chiffre")
            repeat = 0
            break
    print("sortie de boucle")

print(CB_number)
# -------------------------------------------------
# multiplication de chffre de rang impaire
# --------------------------------------------------
CB_number[1] = CB_number[1]*3
CB_number[3] = CB_number[3]*3
CB_number[5] = CB_number[5]*3
CB_number[7] = CB_number[7]*3
CB_number[9] = CB_number[9]*3
CB_number[11] = CB_number[11]*3
# --------------------------------------------------

impair = CB_number[1] + CB_number[3] + CB_number[5] + CB_number[7] + CB_number[9] + CB_number[11]
pair = CB_number[0] + CB_number[2] + CB_number[4] + CB_number[6] + CB_number[8] + CB_number[10]

result = impair + pair
divide = result % 10

if divide != 0:
    result2 = 10 - divide
else:
    result2 = divide


repeat2 = 0

while repeat2 == 0:
    try:
        verif = int(input("entré le 13ème chiffre de votre code barre"))
        repeat2 = 1
    except:
        print("ERREUR : veuillez taper un chiffre")
if verif == result2:
    print("votre code barre est valide")
else:
    print("votre code barre n'est pas valide")

