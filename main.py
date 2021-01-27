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
        print(image.filename)
        print(file[1])
        w, h = image.size

        '''# image.show()
        # The pixel format used by the image. Typical values are "1", "L", "RGB", or "CMYK."
        print(image.mode)  # Output: RGB


        # Image size, in pixels. The size is given as a 2-tuple (width, height).
        print(w)  # Output: (1920, 1280)

        print(h)'''

        if w == h:
            print("la photo " + file + " est carrée et peut être recadrée")
            flag = True
        elif h + h * .10 <= w <= h - h * .10 and not flag:
            print("La photo n'est pas vraiment carrée, mais elle peut quand meme etre resize")
            choix2 = int(input("Appuyez sur 1 pour oui, n'importe quoi d'autre pour non"))
            if choix2 == 1:
                flag = True

        if flag:
            print("Choisissez l'une des deux options")
            choix = int(input("1 : 200*200\n2 : 800*800\n\n"))
            print(choix)
            if choix == 1:
                print("oueoueoue")
                new_image = image.resize((200, 200))
                new_image.save("pictures/" + file.split('.')[0] + "(200x200).jpg")
                print("Image recadrée")
            elif choix == 2:
                new_image = image.resize((800, 800))
                new_image.save("pictures/" + file.split('.')[0] + '(800x800).jpg')
                print("Image recadrée")
            else:
                print("wtf")
        # Colour palette table, if any.
        print(image.palette)  # Output: None

    print(str(i) + " des " + str(len(list_of_pictures)) + " photos disponibles sont carrées")

else:
    print("Veuillez créer un dossier pictures et ajouter des photos dedans. Le script ne détecte aucune photo")
# new_image = image.resize((200, 200))
# new_image.save("image200.jpg")

# print(new_image.size)
