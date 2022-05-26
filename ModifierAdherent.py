from tkinter import *
from subprocess import call

import customtkinter
import mysql.connector
from tkinter import Tk,ttk
from tkinter import messagebox

from PIL import ImageTk,Image

root = Tk()
root.title("Modifier Adherent")
root.geometry('1166x718')
root.resizable(0, 0)


bg_frame = Image.open('images\\background1.png')
photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(root, image=photo)
bg_panel.image = photo
bg_panel.pack(fill='both', expand='yes')

lgn_frame = Frame(root, bg='#040405', width=950, height=650)
lgn_frame.place(x=100, y=35)



db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
mycursor = db.cursor()

labelId = customtkinter.CTkLabel(root,text="Chercher par Id_Adherent",width=120,height=25, bg_color='black')
labelId.place(x=300,y=125)
inputId = Entry(root,width=50,borderwidth=5)
inputId.place(x=500,y=120)
def sel():
    idd = inputId.get()
    nom = inputNom.get()
    prenom = inputPrenom.get()
    dn = inputDN.get()
    adresse = inputAdresse.get()
    email = inputEmail.get()
    tel = inputTele.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    mycursor = db.cursor()
    mycursor.execute("SELECT Nom_Adh FROM adherent WHERE Id_Adh=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputNom.insert(0, data)
    mycursor.execute("SELECT Prenom_Adh FROM adherent WHERE Id_Adh=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputPrenom.insert(1, data)
    mycursor.execute("SELECT DateNaissance_Adh FROM adherent WHERE Id_Adh=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputDN.insert(2, data)
    mycursor.execute("SELECT Adresse_Adh FROM adherent WHERE Id_Adh=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputAdresse.insert(3, data)
    mycursor.execute("SELECT Email_Adh FROM adherent WHERE Id_Adh=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputEmail.insert(4, data)
    mycursor.execute("SELECT Tele_Adh FROM adherent WHERE Id_Adh=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputTele.insert(5, data)

    ii = inputId.get()
    nomm = inputNom.get()
    prenomm = inputPrenom.get()
    dnn = inputDN.get()
    adressee = inputAdresse.get()
    emaill = inputEmail.get()
    tele = inputTele.get()

ButtonSelect = customtkinter.CTkButton(root,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 text="Chercher",
                                 command=sel,
                                 fg_color="grey",
                                 text_color="white"
                                 )
ButtonSelect.place(x=830,y=120)

labelNom = customtkinter.CTkLabel(root,text="Nom Adherent",width=120,height=25, bg_color='black')
labelNom.place(x=300,y=170)
inputNom = Entry(root, width=50, borderwidth=5)
inputNom.place(x=500,y=165)


labelPrenom = customtkinter.CTkLabel(root,text="Prenom Adherent",width=120,height=25, bg_color='black')
labelPrenom.place(x=300,y=220)
inputPrenom = Entry(root, width=50, borderwidth=5)
inputPrenom.place(x=500,y=215)

labelDN = customtkinter.CTkLabel(root,text="Date naissance Adherent",width=120,height=25, bg_color='black')
labelDN.place(x=300,y=270)
inputDN = Entry(root, width=50, borderwidth=5)
inputDN.place(x=500,y=265)

labelAdresse = customtkinter.CTkLabel(root,text="Adresse Adherent",width=120,height=25, bg_color='black')
labelAdresse.place(x=300,y=320)
inputAdresse = Entry(root, width=50, borderwidth=5)
inputAdresse.place(x=500,y=315)

labelEmail = customtkinter.CTkLabel(root,text="Email Adherent",width=120,height=25, bg_color='black')
labelEmail.place(x=300,y=370)
inputEmail = Entry(root, width=50, borderwidth=5)
inputEmail.place(x=500,y=365)

labelTele = customtkinter.CTkLabel(root,text="Telephone Adherent",width=120,height=25, bg_color='black')
labelTele.place(x=300,y=420)
inputTele = Entry(root, width=50, borderwidth=5)
inputTele.place(x=500,y=415)



def modif():
    ii = inputId.get()
    nomm = inputNom.get()
    prenomm = inputPrenom.get()
    dnn = inputDN.get()
    adressee = inputAdresse.get()
    emaill = inputEmail.get()
    tele = inputTele.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    cursor = db.cursor()
    # prepare query and data
    query = (" UPDATE adherent SET Nom_Adh = %s, Prenom_Adh=%s,DateNaissance_Adh=%s,Adresse_Adh=%s,Email_Adh=%s,Tele_Adh=%s WHERE Id_Adh = %s ")
    data = (nomm, prenomm,dnn,adressee,emaill,tele,ii)

    try:
        # update book title
        cursor.execute(query, data)
        messagebox.showinfo("ok","Adherent modifier")
        # accept the changes
        db.commit()

    except Exception as error:
        messagebox.showerror("error","error")
        db.rollback()

ButtonUpdate = customtkinter.CTkButton(root,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 text="Modifier",
                                 command=modif,
                                 fg_color="grey",
                                 text_color="white"
                                 )
ButtonUpdate.place(x=500,y=465)

def back():
    root.destroy()
    call(["python", "menu.py"])


buttonBack = customtkinter.CTkButton(root,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 text="back",
                                 command=back,
                                 fg_color="grey",
                                 text_color="white"
                                 )
buttonBack.place(x=650,y=465)

root.mainloop()