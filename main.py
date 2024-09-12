import PIL.Image
import math

def get_bin_img(src="3-james_bond.png"):
    """Prend en compte le nom idu fichier image source (str)
    Renvoie le tableau binaire de toutes les couleurs"""
    img = PIL.Image.open(src) 
    width, height = img.size
    array = []
    for x in range(width):
        column = []
        for y in range(height):
            r,v,b = img.getpixel((x,y))
            color = [bin(r)[2:],bin(v)[2:],bin(b)[2:]]
            column.append(color)
        array.append(column)
    return array

def get_bin_msg(src="3-message.txt"):
    array = []
    with open(src) as f:
        msg = f.read()
        for letter in msg:
            array.append(bin(ord(letter))[2:])
    return array, len(msg)

def add_zeros(array, nb):
    if(type(array) == list):
        for i in range(len(array)):
            if(len(array[i]) < nb):
                for j in range(nb-len(array[i])):
                    array[i] = "0" + array[i]
    else:
        for i in range(len(array)):
            if(len(array) < nb):
                array = "0" + array

    return array

def insertion(length_msg, img_array, array):
    #Ajout des informations de codage
    index = 0
    for i in range(5):
        for j in range(len(img_array[0][i])):
            length_in_bin = bin(length_msg)[2:]
            length_in_bin = add_zeros(length_in_bin, 15)
            print(length_in_bin)
            print(img_array[0][i][j][:-1] + length_in_bin[j])

img_array = get_bin_img()
array, length_msg = get_bin_msg()
array = add_zeros(array, 8)
insertion(length_msg, img_array, array)