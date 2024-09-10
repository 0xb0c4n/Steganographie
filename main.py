import PIL.Image
import math

def get_bin(src="3-james_bond.png"):
    """Prend en compte le nom du fichier image source (str)
    Renvoie le tableau binaire de toutes les couleurs"""
    img = PIL.Image.open(src)
    width, height = img.size
    for x in range(width+1):
        for y in range(height+1):
            r,v,b = img.getpixel((x,y))
