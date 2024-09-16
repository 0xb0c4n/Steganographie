import PIL.Image


def get_bin_img(src="out.png"):
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
    return img, array

def dernier_bin(oct=None):
    """revois la derniere bit d'un octect"""
    return str(oct)[-1]

def get_nb_char(img_array):
    char_nb = ""
    for i in range(5):
        for j in range(len(img_array[0][i])):
            char_nb += img_array[0][i][j][-1]
    return(int(char_nb, 2))

def mis_en_forme(messageEnLST):
    message= []
    nombreC = 0
    for nbC in range(15):
        nombreC += nbC
    nbCarectere = bin(nombreC)
    message.append(nbCarectere)
    n = 15
    messageVrai = ""
    while  n < len(messageEnLST):
        messageVrai += messageEnLST[n]
        n +=1
    return messageVrai

        

img, img_array = get_bin_img('out.png')
get_nb_char(img_array)