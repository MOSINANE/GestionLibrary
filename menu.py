'''from tkinter import *
from tkinter import Tk, Frame, Menu
import mysql.connector
from subprocess import call
from PIL import Image,ImageTk
import pyautogui
#from tkhtmlview import HTMLLabel
import tkinter as tk
import time
# root window
root = Tk()
root.geometry('2500x1000')
root.title('Menu Bilbiotheque')

#BG
img1 = ImageTk.PhotoImage(Image.open("biblio5.jpg"))
img2 = ImageTk.PhotoImage(Image.open("biblio2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("biblio6.jpg"))
#img4 = ImageTk.PhotoImage(Image.open("biblio4.jpg"))


mylabel = Label(root,font="bold",width=2500,height=2500)
mylabel.pack()
#mylabel.place(x=0,y=0)



x=1
def move():
    global x
    if x == 4:
        x=1
    if x==1:
        mylabel.config(image=img1)
    elif x ==2:
        mylabel.config(image=img2)
    elif x==3:
        mylabel.config(image=img3)
    x+=1
    mylabel.after(2000,move)
move()
#form


# create a menubar
menubar = Menu(root)

root.config(menu=menubar)

# create the file_menu
adherent_menu = Menu(
    menubar,
    tearoff=0
)
livre_menu = Menu(
    menubar,
    tearoff=0
)
auteur_menu = Menu(
    menubar,
    tearoff=0
)
emprunter_menu = Menu(
    menubar,
    tearoff=0
)
ME_menu = Menu(
    menubar,
    tearoff=0
)
TL_menu = Menu(
    menubar,
    tearoff=0
)
EX_menu = Menu(
    menubar,
    tearoff=0
)
#Adherent
def AjouterAdherent():
    root.destroy()
    call(["python", "AjouterAdherent.py"])
def ModifierAdherent():
    root.destroy()
    call(["python", "ModifierAdherent.py"])
def SupprimerAdherent():
    root.destroy()
    call(["python", "SupprimerAdherent.py"])
def AfficherAdherent():
    root.destroy()
    call(["python", "AfficherAdherent.py"])
#Livre
def AjouterLivre():
    root.destroy()
    call(["python", "AjouterLivre.py"])
def ModifierLivre():
    root.destroy()
    call(["python", "ModifierLivre.py"])
def SupprimerLivre():
    root.destroy()
    call(["python", "SupprimerLivre.py"])
def AfficherLivre():
    root.destroy()
    call(["python", "AfficherLivre.py"])
#Auteur
def AjouterAuteur():
    root.destroy()
    call(["python", "AjouterAuteur.py"])
def ModifierAuteur():
    root.destroy()
    call(["python", "ModifierAuteur.py"])
def SupprimerAuteur():
    root.destroy()
    call(["python", "SupprimerAuteur.py"])
def AfficherAuteur():
    root.destroy()
    call(["python", "AfficherAuteur.py"])
#Emprunt
def AjouterEmprunt():
    root.destroy()
    call(["python", "AjouterEmprunt.py"])
def ModifierEmprunt():
    root.destroy()
    call(["python", "ModifierEmprunt.py"])
def SupprimerEmprunt():
    root.destroy()
    call(["python", "SupprimerEmprunt.py"])
def AfficherEmprunt():
    root.destroy()
    call(["python", "AfficherEmprunt.py"])
#ME
def AjouterME():
    root.destroy()
    call(["python", "AjouterME.py"])
def ModifierME():
    root.destroy()
    call(["python", "ModifierME.py"])
def SupprimerME():
    root.destroy()
    call(["python", "SupprimerME.py"])
def AfficherME():
    root.destroy()
    call(["python", "AfficherME.py"])
#TL
def AjouterTL():
    root.destroy()
    call(["python", "AjouterTL.py"])
def ModifierTL():
    root.destroy()
    call(["python", "MlodifiertTL.py"])
def SupprimerTL():
    root.destroy()
    call(["python", "SupprimerTL.py"])
def AfficherTL():
    root.destroy()
    call(["python", "AfficherTL.py"])

#EX
def AjouterEX():
    root.destroy()
    call(["python", "AjouterExemplaire.py"])
def ModifierEX():
    root.destroy()
    call(["python", "ModifierExemplaire.py"])
def SupprimerEX():
    root.destroy()
    call(["python", "SupprimerExemplaire.py"])
def AfficherEX():
    root.destroy()
    call(["python", "AfficherExemplaire.py"])
# add menu items to the File menu
adherent_menu.add_command(label='Ajouter',command=AjouterAdherent)
adherent_menu.add_command(label='Modifier',command=ModifierAdherent)
adherent_menu.add_command(label='Supprimer',command=SupprimerAdherent)
adherent_menu.add_command(label='Afficher',command=AfficherAdherent)
#adherent_menu.add_separator()
livre_menu.add_command(label='Ajouter', command=AjouterLivre)
livre_menu.add_command(label='Modifier',command=ModifierLivre)
livre_menu.add_command(label='Supprimer',command=SupprimerLivre)
livre_menu.add_command(label='Afficher',command=AfficherLivre)
#livre_menu.add_separator()
auteur_menu.add_command(label='Ajouter',command=AjouterAuteur)
auteur_menu.add_command(label='Modifier',command=ModifierAuteur)
auteur_menu.add_command(label='Supprimer',command=SupprimerAuteur)
auteur_menu.add_command(label='Afficher',command=AfficherAuteur)
#auteur_menu.add_separator()
emprunter_menu.add_command(label='Ajouter',command=AjouterEmprunt)
emprunter_menu.add_command(label='Modifier',command=ModifierEmprunt)
emprunter_menu.add_command(label='Supprimer',command=SupprimerEmprunt)
emprunter_menu.add_command(label='Afficher',command=AfficherEmprunt)
#ME_menu.add_separator()
ME_menu.add_command(label='Ajouter',command=AjouterME)
ME_menu.add_command(label='Modifier',command=ModifierME)
ME_menu.add_command(label='Supprimer',command=SupprimerME)
ME_menu.add_command(label='Afficher',command=AfficherME)
#TL_menu.add_separator()
TL_menu.add_command(label='Ajouter',command=AjouterTL)
TL_menu.add_command(label='Modifier',command=ModifierTL)
TL_menu.add_command(label='Supprimer',command=SupprimerTL)
TL_menu.add_command(label='Afficher',command=AfficherTL)
#EX_menu.add_separator()
EX_menu.add_command(label='Ajouter',command=AjouterEX)
EX_menu.add_command(label='Modifier',command=ModifierEX)
EX_menu.add_command(label='Supprimer',command=SupprimerEX)
EX_menu.add_command(label='Afficher',command=AfficherEX)

#emprunter_menu.add_separator()
# add Exit menu item
''''''adherent_menu.add_command(
    label='Exit',
    command=root.destroy
)''''''
# add the File menu to the menubar
menubar.add_cascade(
    label="Adherent",
    menu=adherent_menu
)
menubar.add_cascade(
    label="Livre",
    menu=livre_menu
)
menubar.add_cascade(
    label="Auteur",
    menu=auteur_menu
)
menubar.add_cascade(
    label="Emprunt",
    menu=emprunter_menu
)
menubar.add_cascade(
    label="Maison Edition",
    menu=ME_menu
)
menubar.add_cascade(
    label="Type Livre",
    menu=TL_menu
)
menubar.add_cascade(
    label="Exemplaire",
    menu=EX_menu
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

# add the Help menu to the menubar
menubar.add_cascade(
    label="Exit",
    command=root.destroy
)

root.mainloop()'''

from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
from subprocess import call
from tkinter import Tk,ttk
import pyautogui
import time
root = Tk()
root.geometry('1166x718')
root.resizable(0, 0)
#root.state('zoomed')
root.title('Menu Bilbiotheque')
# create a menubar
menubar = Menu(root)

root.config(menu=menubar)

# create the file_menu
adherent_menu = Menu(
    menubar,
    tearoff=0
)
livre_menu = Menu(
    menubar,
    tearoff=0
)
auteur_menu = Menu(
    menubar,
    tearoff=0
)
emprunter_menu = Menu(
    menubar,
    tearoff=0
)
ME_menu = Menu(
    menubar,
    tearoff=0
)
TL_menu = Menu(
    menubar,
    tearoff=0
)
EX_menu = Menu(
    menubar,
    tearoff=0
)
#Adherent
def AjouterAdherent():
    root.destroy()
    call(["python", "AjouterAdherent.py"])
def ModifierAdherent():
    root.destroy()
    call(["python", "ModifierAdherent.py"])
def SupprimerAdherent():
    root.destroy()
    call(["python", "SupprimerAdherent.py"])
def AfficherAdherent():
    root.destroy()
    call(["python", "AfficherAdherent.py"])
#Livre
def AjouterLivre():
    root.destroy()
    call(["python", "AjouterLivre.py"])
def ModifierLivre():
    root.destroy()
    call(["python", "ModifierLivre.py"])
def SupprimerLivre():
    root.destroy()
    call(["python", "SupprimerLivre.py"])
def AfficherLivre():
    root.destroy()
    call(["python", "AfficherLivre.py"])
#Auteur
def AjouterAuteur():
    root.destroy()
    call(["python", "AjouterAuteur.py"])
def ModifierAuteur():
    root.destroy()
    call(["python", "ModifierAuteur.py"])
def SupprimerAuteur():
    root.destroy()
    call(["python", "SupprimerAuteur.py"])
def AfficherAuteur():
    root.destroy()
    call(["python", "AfficherAuteur.py"])
#Emprunt
def AjouterEmprunt():
    root.destroy()
    call(["python", "AjouterEmprunt.py"])
def ModifierEmprunt():
    root.destroy()
    call(["python", "ModifierEmprunt.py"])
def SupprimerEmprunt():
    root.destroy()
    call(["python", "SupprimerEmprunt.py"])
def AfficherEmprunt():
    root.destroy()
    call(["python", "AfficherEmprunt.py"])
#ME
def AjouterME():
    root.destroy()
    call(["python", "AjouterME.py"])
def ModifierME():
    root.destroy()
    call(["python", "ModifierME.py"])
def SupprimerME():
    root.destroy()
    call(["python", "SupprimerME.py"])
def AfficherME():
    root.destroy()
    call(["python", "AfficherME.py"])
#TL
def AjouterTL():
    root.destroy()
    call(["python", "AjouterTL.py"])
def ModifierTL():
    root.destroy()
    call(["python", "MlodifiertTL.py"])
def SupprimerTL():
    root.destroy()
    call(["python", "SupprimerTL.py"])
def AfficherTL():
    root.destroy()
    call(["python", "AfficherTL.py"])

#EX
def AjouterEX():
    root.destroy()
    call(["python", "AjouterExemplaire.py"])
def ModifierEX():
    root.destroy()
    call(["python", "ModifierExemplaire.py"])
def SupprimerEX():
    root.destroy()
    call(["python", "SupprimerExemplaire.py"])
def AfficherEX():
    root.destroy()
    call(["python", "AfficherExemplaire.py"])
# add menu items to the File menu
adherent_menu.add_command(label='Ajouter',command=AjouterAdherent)
adherent_menu.add_command(label='Modifier',command=ModifierAdherent)
adherent_menu.add_command(label='Supprimer',command=SupprimerAdherent)
adherent_menu.add_command(label='Afficher',command=AfficherAdherent)
#adherent_menu.add_separator()
livre_menu.add_command(label='Ajouter', command=AjouterLivre)
livre_menu.add_command(label='Modifier',command=ModifierLivre)
livre_menu.add_command(label='Supprimer',command=SupprimerLivre)
livre_menu.add_command(label='Afficher',command=AfficherLivre)
#livre_menu.add_separator()
auteur_menu.add_command(label='Ajouter',command=AjouterAuteur)
auteur_menu.add_command(label='Modifier',command=ModifierAuteur)
auteur_menu.add_command(label='Supprimer',command=SupprimerAuteur)
auteur_menu.add_command(label='Afficher',command=AfficherAuteur)
#auteur_menu.add_separator()
emprunter_menu.add_command(label='Ajouter',command=AjouterEmprunt)
emprunter_menu.add_command(label='Modifier',command=ModifierEmprunt)
emprunter_menu.add_command(label='Supprimer',command=SupprimerEmprunt)
emprunter_menu.add_command(label='Afficher',command=AfficherEmprunt)
#ME_menu.add_separator()
ME_menu.add_command(label='Ajouter',command=AjouterME)
ME_menu.add_command(label='Modifier',command=ModifierME)
ME_menu.add_command(label='Supprimer',command=SupprimerME)
ME_menu.add_command(label='Afficher',command=AfficherME)
#TL_menu.add_separator()
TL_menu.add_command(label='Ajouter',command=AjouterTL)
TL_menu.add_command(label='Modifier',command=ModifierTL)
TL_menu.add_command(label='Supprimer',command=SupprimerTL)
TL_menu.add_command(label='Afficher',command=AfficherTL)
#EX_menu.add_separator()
EX_menu.add_command(label='Ajouter',command=AjouterEX)
EX_menu.add_command(label='Modifier',command=ModifierEX)
EX_menu.add_command(label='Supprimer',command=SupprimerEX)
EX_menu.add_command(label='Afficher',command=AfficherEX)

#emprunter_menu.add_separator()
# add Exit menu item
'''adherent_menu.add_command(
    label='Exit',
    command=root.destroy
)'''
# add the File menu to the menubar
menubar.add_cascade(
    label="Adherent",
    menu=adherent_menu
)
menubar.add_cascade(
    label="Livre",
    menu=livre_menu
)
menubar.add_cascade(
    label="Auteur",
    menu=auteur_menu
)
menubar.add_cascade(
    label="Emprunt",
    menu=emprunter_menu
)
menubar.add_cascade(
    label="Maison Edition",
    menu=ME_menu
)
menubar.add_cascade(
    label="Type Livre",
    menu=TL_menu
)
menubar.add_cascade(
    label="Exemplaire",
    menu=EX_menu
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

# add the Help menu to the menubar
menubar.add_cascade(
    label="Exit",
    command=root.destroy
)

bg_frame = Image.open('images\\background1.png')
photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(root, image=photo)
bg_panel.image = photo
bg_panel.pack(fill='both', expand='yes')
# ====== Login Frame =========================
lgn_frame = Frame(root, bg='Black', width=950, height=600)
lgn_frame.place(x=100, y=60)

labelii = Label(root,text="Bienvenu à votre espace bibliotheque", font=("Arial Black", 15), bg="Black", fg="White")
labelii.place(x=300,y=300)



root.mainloop()

''' class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
      #  self.window.state('zoomed')
        self.window.title('Authentification')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=100, y=70)


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()'''