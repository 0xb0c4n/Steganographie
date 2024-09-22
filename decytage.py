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

def dernier_bin(octt=None):
    """revois la derniere bit d'un octect"""
    oct = str(octt) 
    rang_fin = len(oct)
    dernier_bin[rang_fin] = oct
    return dernier_bin


def decyptage(lst_bin='binaire', image = '3-james_bond'):
    """Renvois une list avec le message inscris dans l'image"""
    img = PIL.open(image)
    h, l = img.size
    h_compte, l_compte = 0 , 0
    messageEnLST = []
    while h_compte and l_compte < l:
        for rangcol in range(3):
            for oct in lst_bin:
                mes = dernier_bin(oct[bin][rangcol]) 
            messageEnLST.append(str(mes))
        h_compte +=1
        l_compte +=1
    return messageEnLST

def mis_en_forme(messageEnLST):
    message= []
    nombreC = 0
    for nbC in range(15):
        nombreC += nbC
    nbCarectere = bin(nombreC)
    message.append(nbCarectere)
    rangC = 15
    while  rangC < len(messageEnLST):
        message_str = ""
        message_bin = 0
        for i in range():
            pass
        rangC +=8 
        pass


print(binaire('3-james_bond.png'))
