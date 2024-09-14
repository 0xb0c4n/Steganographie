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
            length_in_bin = add_zeros(bin(length_msg)[2:],15)

            img_array[0][i][j] = list(img_array[0][i][j][:-1])
            img_array[0][i][j].append(length_in_bin[index])
            img_array[0][i][j] = "".join(img_array[0][i][j])
            index+=1
    #Encodage du message
    index_msg = 0
    for i in range(len(img_array)):
        if i == 0:
            for j in range(len(img_array[i])):
                for k in range(len(img_array[i][j])):
                    if index_msg < length_msg:
                        copy = list(img_array[i][j][k][:-1])
                        string = "".join(array)
                        copy.append(string[index_msg])
                        index_msg += 1
        else:
            for j in range(len(img_array[i])):
                for k in range(len(img_array[i][j])):
                    if index_msg < length_msg:
                        copy = list(img_array[i][j][k][:-1])
                        string = "".join(array)
                        copy.append(string[index_msg])
                        index_msg += 1

                    
img_array = get_bin_img()
array, length_msg = get_bin_msg()
array = add_zeros(array, 8)
insertion(length_msg, img_array, array)