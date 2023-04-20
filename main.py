# Creado el 20 de Abril de 2023 por José Luis Santos Mendoza
# Actividad 6: hilos
# Universidad de Guadalajara, Seminario de Solución de Problemas de Sistemas Operativos
# Profesor Javier Rosales Martínez, Sección D06

from tkinter import *
from PIL import Image, ImageTk


# Resizing the images
def resizeImages(image1, image2):
    width1, height1 = image1.size
    width2, height2 = image2.size
    if width1 != width2 or height1 != height2:
        max_width = min(width1, width2)
        max_height = min(height1, height2)
        image1 = image1.resize((max_width, max_height))
        image2 = image2.resize((max_width, max_height))
    return image1, image2


# Resizing the main window
def resizeWindow(root, width, height):
    root.geometry(f"{width}x{height}")


# Window config
root = Tk()
root.title("Moviendo imágenes con Tkinter")
resizeWindow(root, 800, 800)

# Charging images
image1 = Image.open("imagen1.png")
image2 = Image.open("imagen2.png")

# Resizing images
image1, image2 = resizeImages(image1, image2)

# Creating an PhotoImage object
tkImage1 = ImageTk.PhotoImage(image1)
tkImage2 = ImageTk.PhotoImage(image2)

# Creating labels to show the images
label1 = Label(root, image=tkImage1)
label2 = Label(root, image=tkImage2)

# Variables to control the direction of the movement
dir1 = 1
dir2 = 1


# Moving image1 from top to bottom
def moveImage1():
    global dir1
    x, y = label1.winfo_x(), label1.winfo_y()
    if y > 550:
        dir1 = -1
    elif y < 0:
        dir1 = 1
    y += 10 * dir1
    label1.place(x=x, y=y)
    root.after(50, moveImage1)


# Moving image2 from left to the right
def moveImage2():
    global dir2
    x, y = label2.winfo_x(), label2.winfo_y()
    if x > 550:
        dir2 = -1
    elif x < 0:
        dir2 = 1
    x += 10 * dir2
    label2.place(x=x, y=y)
    root.after(50, moveImage2)


# Starting images movement
moveImage1()
moveImage2()

# Showing labels on the window
label1.pack()
label2.pack()

# Executing the main window
root.mainloop()
