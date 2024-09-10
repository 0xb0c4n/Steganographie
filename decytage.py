import PIL.Image as PIL 


def binaire(image='3-james_bond.png'):
    """Renvois une list avec 
    la position du pixel et la couleur du pixel en binaire"""
    img = PIL.open(image)
    h , l = img.size
    h_compte , l_compte = 0 , 0
    lst_bin = []
    while h_compte < h and l_compte < l:
        r, v, b = img.getpixel((h_compte,l_compte))
        bin_colR = bin(r)[2:]
        bin_colV = bin(v)[2:]
        bin_colB = bin(b)[2:]
        dic_binCol = {'pixel : ': (h_compte, l_compte),'bin : ': [bin_colR, bin_colV, bin_colB] }
        lst_bin.append(dic_binCol)
        h_compte +=1
        l_compte +=1
    return lst_bin

def decyptage(lst_bin='binaire', image = '3-james_bond'):
    """Renvois un str avec le message inscris dans l'image"""
    img = PIL.open(image)
    h, l = img.size
    h_compte, l_compte = 0 , 0
    message = ""
    while h_compte and l_compte < l:

        for rang in range(len(lst_bin)+1):
            for colonne in range(len(lst_bin[rang]['bin'])+1):
                bin_actuel = lst_bin[rang]['bin'][colonne] 
        h_compte +=1
        l_compte +=1

print(binaire('3-james_bond.png'))
