#!/usr/bin/python3

import PIL.Image

def get_bin_img_d(src="out.png"):
    """Prend en compte le nom du fichier image source (str)
    Renvoie le tableau binaire de toutes les couleurs"""
    img = PIL.Image.open(src) 
    width, height = img.size
    array = []
    for x in range(width):
        i = []
        for y in range(height):
            r,v,b = img.getpixel((x,y))
            j = [bin(r)[2:],bin(v)[2:],bin(b)[2:]]
            i.append(j)
        array.append(i)
    return array


def get_nb_char(img_array):
    """Prend en paramètre l'image (sous forme d'une liste avec les couleurs de chaque pixel en binaire)
    Renvoie la taille récupérée du message encodé"""
    char_nb = ""
    for i in range(5):
        for j in range(len(img_array[0][i])):
            char_nb += img_array[0][i][j][-1]
    return(int(char_nb, 2))

def mis_en_forme(img_array,nb_char):
    """Prend en paramètre l'image (sous forme d'une liste avec les couleurs de chaque pixel en binaire) et le nombre de caractères du message
    Renvoie le message décodé en binaire """
    messageVrai = ""
    index = 0

    for i in range(len(img_array)):
        if i == 0:
            for j in range(5, len(img_array[i])):
                for k in range(len(img_array[i][j])):
                    if nb_char*8 > index:
                        messageVrai += img_array[i][j][k][-1]
                        index += 1
                    else:
                        break
        else:
            for j in range(len(img_array[i])):
                for k in range(len(img_array[i][j])):
                    if nb_char*8 > index:
                        messageVrai += img_array[i][j][k][-1]
                        index += 1
                    else:
                        break
        
    o = []
    while messageVrai:
        o.append(messageVrai[:8])
        messageVrai = messageVrai[8:]
    return o

        
def decrypte():
    """Ne prend rien en paramètre
    Renvoie le message transformé de binaire en str"""
    img_array = get_bin_img_d()
    nb_char = get_nb_char(img_array)
    result = mis_en_forme(img_array, nb_char)
    decoded_str = ""
    for elt in result:
        decoded_str += chr(int(elt, 2))
    print("\n" + decoded_str)
    return decoded_str
