from PIL import Image
import glob

i = 0
flag = False

list_of_pictures = glob.glob('pictures/*.jpg')
if len(list_of_pictures) != 0:
    print("il y a " + str(len(list_of_pictures)) + " photos dans le dossier\n")
    for picture in list_of_pictures:
        image = Image.open(picture)
        # The file format of the source file.
        print(image.format)  # Output: JPEG

        file = image.filename.split('\\')[1]
        print(file)
        w, h = image.size

        if w == h:  # Check if the photo's resolution is square
            print("la photo " + file + " est carrée et peut être recadrée")
            flag = True
        elif (h - h * .10) <= w <= (h + h * .10):  # if it's not square, it will check if the width is within a 10%
            # margin of the height
            # im bad at explaining
            print("La photo" + file + " n'est pas vraiment carrée, mais elle peut quand même être resize sans « effouarage »")
            choix2 = int(input("Appuyez sur 1 pour oui, n'importe quel autre chiffre pour non\n"))  # asking user
            if choix2 == 1:
                flag = True
        else:
            flag = False
            print("Cette photo ne peut définitivement pas être recadrée")

        if flag:
            print("Choisissez l'une des trois options")
            choix = int(input("1 : 200*200 et 800*800\n2 : Ne rien faire\n\n"))
            if choix == 1:
                new_image = image.resize((200, 200))
                new_image.save("pictures/" + file.split('.')[0] + "(200x200).jpg")
                print("Image recadrée")
                new_image = image.resize((800, 800))
                new_image.save("pictures/" + file.split('.')[0] + '(800x800).jpg')
                print("Image recadrée")
            elif choix == 2:
                print("okok")
        print("\n\n")

else:
    print("Veuillez créer un dossier pictures et ajouter des photos en jpg dedans. Le script ne détecte aucune photo "
          "dans ce format")
