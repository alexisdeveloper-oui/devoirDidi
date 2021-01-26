from PIL import Image
import glob

i = 0
# filename = input("Entrez le nom de la photo : ")

list_of_pictures = glob.glob('pictures/*.jpg')
if len(list_of_pictures) != 0:
    for picture in list_of_pictures:
        image = Image.open(picture)
        # The file format of the source file.
        print(image.format)  # Output: JPEG

        file = image.filename.split('\\')
        print(image.filename)
        print(file[1])
        # image.show()
        # The pixel format used by the image. Typical values are "1", "L", "RGB", or "CMYK."
        print(image.mode)  # Output: RGB

        w, h = image.size

        # Image size, in pixels. The size is given as a 2-tuple (width, height).
        print(w)  # Output: (1920, 1280)

        print(h)
        if w == h:
            print("cette image est carrée et peut être recadrée")
            i += 1
        # Colour palette table, if any.
        print(image.palette)  # Output: None

    print(str(i) + " des " + str(len(list_of_pictures)) + " photos disponibles sont carrées")

else:
    print("Veuillez svp créer un dossier pictures et ajouter des photos dedans. Le script ne détecte aucune photo")
# new_image = image.resize((200, 200))
# new_image.save("image200.jpg")

# print(new_image.size)
