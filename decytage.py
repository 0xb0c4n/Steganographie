import PIL.Image as PIL 

def binaire(image):
    """Renvois un str avec le message cacher dans l'image"""
    img = PIL.open(image)
    h , l = img.size
    h_compte , l_compte = 0 , 0
    lst_bin = []
    while h_compte <= h and l_compte <= l:
        r, v, b = img.getpixel((h_compte,l_compte))
        bin_colR = bin(r)[2:]
        bin_colV = bin(v)[2:]
        bin_colB = bin(b)[2:]
        dic_binCol = {'pixel : ': (h_compte, l_compte),' couleur : ': (r, v, b), 'bin : ': [bin_colR, bin_colV, bin_colB] }
        lst_bin.append(dic_binCol)
        h_compte +=1
        l_compte +=1
    return lst_bin


print(binaire('3-james_bond.png'))
