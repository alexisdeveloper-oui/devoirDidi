from PIL import Image
import glob

i = 0
flag = False
# filename = input("Entrez le nom de la photo : ")

list_of_pictures = glob.glob('pictures/*.jpg')
if len(list_of_pictures) != 0:
    for picture in list_of_pictures:
        image = Image.open(picture)
        # The file format of the source file.
        print(image.format)  # Output: JPEG

        file = image.filename.split('\\')[1]
        print(file)
        w, h = image.size

        if w == h: #Check if the photo's resolution is square
            print("la photo " + file + " est carrée et peut être recadrée")
            flag = True
        elif (h - h * .10) <= w <= (h + h * .10): #if it's not square, it will check if the width is within 10% of the height
            print("La photo n'est pas vraiment carrée, mais elle peut quand même être resize sans « effouarage »")
            choix2 = int(input("Appuyez sur 1 pour oui, n'importe quel autre chiffre pour non\n")) #asking user
            if choix2 == 1:
                flag = True
        else:
            flag = False
            print("Cette photo ne peut définitivement pas être recadrée")

        if flag:
            print("Choisissez l'une des trois options")
            choix = int(input("1 : 200*200\n2 : 800*800\n3 : Ne rien faire\n\n"))
            if choix == 1:
                print("oueoueoue")
                new_image = image.resize((200, 200))
                new_image.save("pictures/" + file.split('.')[0] + "(200x200).jpg")
                print("Image recadrée")
            elif choix == 2:
                new_image = image.resize((800, 800))
                new_image.save("pictures/" + file.split('.')[0] + '(800x800).jpg')
                print("Image recadrée")
            elif choix == 3:
                print("Understandable, have a nice day")

        print("\n\n")

    print(str(i) + " des " + str(len(list_of_pictures)) + " photos disponibles sont carrées")

else:
    print("Veuillez créer un dossier pictures et ajouter des photos en jpg dedans. Le script ne détecte aucune photo "
          "dans ce format")
# new_image = image.resize((200, 200))
# new_image.save("image200.jpg")

# print(new_image.size)
