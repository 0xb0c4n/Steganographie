import PIL.Image
import math

def get_bin_img(src="3-james_bond.png"):
    """Prend en compte le nom du fichier image source (str)
    Renvoie le tableau binaire de toutes les couleurs"""
    img = PIL.Image.open(src)
    width, height = img.size
    array=[]
    for y in range(height):
        rank = []
        for x in range(width):
            r,v,b = img.getpixel((x,y))
            color = [bin(r)[2:],bin(v)[2:],bin(b)[2:]]
            rank.append(color)
        array.append(rank)
    return array

def get_bin_msg(src="3-message.txt"):
    with open(src) as f:
        print(f.read())

get_bin_msg()
