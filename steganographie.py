import numpy as np
from PIL import Image

def hide(message,image_name):
    image= Image.open(image_name)
    data= asarray(image)

    final_message=""
    for character in message:
        position_ascii=ord(character)
        binaire=bin(position_ascii)[2:]
        while len(binaire)<8:
            binaire= "0" + binaire
        final_message += binaire
    print("{}".format(final_message))


    longueur=len(final_message)
    binaire=bin(longueur)[2:]
    while len(binaire)<16:
        binaire="0"+ binaire
    print("taille a coder:",binaire)
    result_message= binaire = final_message

    #data[y][x][rgb]
    tour=0
    y=0
    for line in data:
        x=0
        for colonne in line:
            rgb=0
            for color in colonne:
                valeur=data[y][x][rgb]
                binaire=bin(valeur)[2:]
                binaire_list=list(binaire)
                del binaire_list(-1)
                binaire_list.append(result_message[tour])
                decimal=int("".joint(binaire_list),2)
                data[y][x][rgb]=decimal
                tour +=1
                rgb+=1
                if tour >= len(result_message):
                    break
            x +=1
            if tour >= len(result_message):
                    break
        y+=1
        if tour >= len(result_message):
            break
    imagefinal= Image.fromarray(data)
    imagefinal.save("secret.png")