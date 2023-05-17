import tkinter as tk
from tkinter import *
ventana = tk.Tk()  
ventana.geometry("500x300+0+0") 
ventana.title("Calculadora")
ventana.resizable(0,0)

def suma():
    n1= int(num.get())
    n2= int(num2.get())
    resul.set(n1+n2)
    signo.set("+")

def resta():
    n1= int(num.get())
    n2= int(num2.get())
    resul.set(n1-n2)
    signo.set("-")

def multi():
    n1= int(num.get())
    n2= int(num2.get())
    resul.set(n1*n2)
    signo.set("*")

def divi():
    n1= int(num.get())
    n2= int(num2.get())
    resul.set(n1/n2)
    signo.set("/")

## Declarar las variables que utilizaremos a StringVar
num = StringVar()
num.set("0")

num2 = StringVar()
num2.set("0")

resul = StringVar()
resul.set("0")

signo = StringVar()
signo.set("")

#Establecer widgets
frame = tk.Frame(ventana, width=500, height=150)
frame.pack()
labelframe1 = tk.LabelFrame(frame, text="Operaciones", width=448, height=130) 
labelframe1.pack()
labelframe2 = tk.LabelFrame(frame, text="Operadores aritmeticos", width=448, height=120)  
labelframe2.pack()

## Contenedor 1
label_n1 = tk.Label(labelframe1, text="Número 1") 
label_n1.place(x=41, y=31)
label_n1.config(font=("Comic Sans MS",13), fg="Red")

label_n2 = tk.Label(labelframe1, text="Número 2") 
label_n2.place(x=200, y=31)
label_n2.config(font=("Comic Sans MS",13), fg="Blue")


label_resul = tk.Label(labelframe1, text="Resultado") 
label_resul.place(x=343, y=31)
label_resul.config(font=("Comic Sans MS",13), fg="Green")

mas = tk.Label(labelframe1, text="", textvariable=signo)
mas.place(x=140, y=60)
mas.config(font=("Comic Sans MS",13), fg="Orange")

igual = tk.Label(labelframe1, text="=") 
igual.place(x=290, y=60)
igual.config(font=("Comic Sans MS",13), fg="Blue")

entrada_n1 = tk.Entry(labelframe1, width=17, textvariable=num) 
entrada_n1.place(x=25, y=60)


entrada_n2 = tk.Entry(labelframe1, width=17, textvariable=num2)
entrada_n2.place(x=170, y=60)

entrada_re = tk.Entry(labelframe1, width=17, textvariable=resul)
entrada_re.place(x=320, y=60)

# Contenedor 2 "Botones"
btn_mas = tk.Button(labelframe2, text="+", width=8, command=suma)
btn_mas.place(x= 25, y=35)
btn_mas.config(font=("Arial",11), fg="Red")

btn_menos = tk.Button(labelframe2, text="-", width=8, command=resta)
btn_menos.place(x=250, y=35)
btn_menos.config(font=("Arial",11), fg="Orange")

btn_multi = tk.Button(labelframe2, text="*", width=8, command= multi)
btn_multi.place( x=140, y=35)
btn_multi.config(font=("Arial",11), fg="Green")


btn_divi = tk.Button(labelframe2, text="/", width=8, command= divi)
btn_divi.place(x=355, y=35)
btn_divi.config(font=("Arial",11), fg="Blue")


mainloop()  
