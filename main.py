import PIL.Image
import math

def get_bin_img(src="3-james_bond.png"):
    """Prend en compte le nom idu fichier image source (str)
    Renvoie le tableau binaire de toutes les couleurs"""
    img = PIL.Image.open(src) 
    width, height = img.size
    array = []
    for y in range(height):
        rank = []
        for x in range(width):
            r,v,b = img.getpixel((x,y))
            color = [bin(r)[2:],bin(v)[2:],bin(b)[2:]]
            rank.append(color)
        array.append(rank)
    return array

def get_bin_msg(src="3-message.txt"):
    array = []
    with open(src) as f:
        msg = f.read()
        for letter in msg:
            array.append(bin(ord(letter))[2:])
    return array

def add_zeros(array):
    for i in range(len(array)):
        if(len(array[i]) < 8):
            for j in range(8-len(array[i])):
                array[i] = "0" + array[i]
    print(array)

array = get_bin_msg()
add_zeros(array)