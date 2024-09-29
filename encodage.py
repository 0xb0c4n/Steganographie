#!/usr/bin/python3

import PIL.Image
import math

def get_bin_img(src="3-james_bond.png"):
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

def turn_to_int(binary):
    """Renvoie le binaire converti en integer
    Prend en paramètre un binaire de type array"""
    return int(str(binary), 2)

def get_img_back(img_array, src="3-james_bond.png"):
    """Effectue l'enregistrement de l'image encodée dans le fichier out.png
    Prend en paramètre l'image encodée (sous forme de liste d'élements binaire) ainsi que la source du fichier"""
    img = PIL.Image.open(src) 
    width, height = img.size

    for x in range(len(img_array)):
        for y in range(len(img_array[x])):
            img_array[x][y] = map(turn_to_int, img_array[x][y])
            img_array[x][y] = tuple(img_array[x][y])
            img.putpixel((x,y), img_array[x][y])
    
    img.save("out.png")
    print("\n Fichier sauvegardé en : out.png")
    img.close()

def get_bin_msg(src="3-message.txt"):
    """Prend en paramètre le message source et va récupérer son contenu
    Renvoie la liste du message avec chaque lettre en binaire (list) ainsi que sa taille (int)"""
    array = []
    with open(src) as f:
        msg = f.read()
        for letter in msg:
            array.append(bin(ord(letter))[2:])
    return array, len(msg)

def add_zeros(array, n):
    """Renvoie soit une liste soit un str d'un élément avec n zéros avant
    Prend en paramètre l'élement (list ou str) et l'entier n de zéros à rajouter"""
    if(type(array) == list):
        for i in range(len(array)):
            if(len(array[i]) < n):
                for j in range(n-len(array[i])):
                    array[i] = "0" + array[i]
    else:
        while n > len(array):
            array = "0" + array

    return array

def insertion(length_msg, img_array, array):
    """Insère le message dans la liste de l'image et renvoie cette même liste encodée
    Prend en paramètre la longueur du message (int), la liste de l'image (list) et la liste du message (list)"""

    #Ajout des informations de codage
    index = 0
    for i in range(5):
        for j in range(len(img_array[0][i])):
            length_in_bin = add_zeros(bin(length_msg)[2:],15)
            img_array[0][i][j] = list(img_array[0][i][j][:-1])
            img_array[0][i][j].append(length_in_bin[index])
            img_array[0][i][j] = "".join(img_array[0][i][j])
            index+=1
    #Encodage du message
    index_msg = 0
    string = "".join(array)
    for i in range(len(img_array)):
        if i == 0:
            for j in range(5,len(img_array[i])):
                for k in range(len(img_array[i][j])):
                    if index_msg < length_msg*8:
                        copy = list(img_array[i][j][k][:-1])
                        copy.append(string[index_msg])
                        img_array[i][j][k] = "".join(copy)
                        index_msg += 1
        else:
            for j in range(len(img_array[i])):
                for k in range(len(img_array[i][j])):
                    if index_msg < length_msg*8:
                        copy = list(img_array[i][j][k][:-1])
                        copy.append(string[index_msg])
                        img_array[i][j][k] = "".join(copy)
                        index_msg += 1

    return img_array


def encodage():  
    """Encode le message dans l'image"""           
    img_array = get_bin_img()
    array, length_msg = get_bin_msg()
    array = add_zeros(array, 8)
    img_array = insertion(length_msg, img_array, array)
    get_img_back(img_array)
    
