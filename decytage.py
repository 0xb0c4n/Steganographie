import PIL.Image as PIL 

def decypte(image):
    """Renvois un str avec le message cacher dans l'image"""
    img = PIL.open(image)
    h , l = img.size
    h_compte , l_compte = 0 , 0