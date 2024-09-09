# import de la librairie PIL
import PIL.Image

# ouverture du fichier :
img = PIL.Image.open('james_bond.png')

# lecture dans le fichier de la taille de l'image
largeur, hauteur = img.size
print("largeur: ", largeur, " hauteur:", hauteur)

# Lecture des couleurs du pixel de coordonnées (0,0)
r, v, b = img.getpixel( (0, 0) )
print('pixel : ', (0,0),' couleur : ', (r, v, b))

# modification en noir, rgb = (0, 0, 0), de la couleur du pixel de coordonnées (10,10)
img.putpixel((10, 10), (0, 0, 0))

# sauvegarde et fermeture du fichier image
img.save('out.png')
img.close()

# ré-ouverture et affichage de l'image
img = PIL.Image.open('out.png')
img.show()
