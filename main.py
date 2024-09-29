from pyfiglet import Figlet
from encodage import *
from decryptage import *

f = Figlet(font='slant')
print(f.renderText('Steganographie'))
print("par 0xb0c4n et 0q3i \n\n")

print("1. Encoder un message")
print("2. Déchiffrer un message")
print("3. Aide")

choice = int(input("Choisissez votre mode :"))

if choice == 1:
    encodage()
elif choice == 2:
    decrypte()
else:
    print("Pour encoder : veuillez entrer le texte souhaité dans le fichier 3-message.txt, l'image dans laquelle sera encodé le fichier sera par défaut 3-james_bond.png.")
    print("Pour déchiffrer : le fichier par défaut sera out.png, à modifier dans decryptage.py dans la première fonction.")