from tkinter import *
from tkinter.ttk import *
 
#Creacion de interfaz grafica con tkinter


index=Tk()
index.title("LOGIN")
index.geometry("300x150")
index.resizable(width=False, height=False)

luser=Label(index, text="Ingrese nombre de usuario:")
luser.pack()

user=StringVar()
euser=Entry(index, width=30, textvariable=user)
euser.pack()

lpas=Label(index, text="Password:")
lpas.pack()

pas=StringVar()
epas=Entry(index, width=30, textvariable=pas, show="*")
epas.pack()

def ingresar():
    if user.get()=="chres" and pas.get()=="pantufla24": #Datos de administrador
        index.title("Usted ingreso como administrador")

    else:
        index.title("Usuario incorrecto")
   
b1=Button(index, text="Entrar", command=ingresar)
b1.pack(side=BOTTOM)

index.mainloop()
