import tkinter as tk
import math
import re
from tkinter import *
ventana = tk.Tk()  
ventana.geometry("375x472+0+0") 
ventana.title("Calculadora")
ventana.resizable(0,0)

# Función entrada
def limpiar():
    operador = ""
    sali.set(operador)

def borrarUno():
    operador = sali.get()
    operador = operador.rstrip(operador[-1])  # Eliminar el último carácter
    sali.set(operador)

def entrada(val):
    operador = sali.get()
    if val == 'sqrt':
        try:
            resultado = math.sqrt(float(operador))
        except ValueError:
            resultado = 'Error'
        sali.set(resultado)
    else:
        operador = re.sub(r'[-+*/]{2,}', lambda match: match.group(0)[-1], operador + val)
        sali.set(operador )


def resultado():
    try:
        operador = sali.get()
        op = eval(operador)
    except Exception as er:
        limpiar()
        op = (f"Error:", er)
    sali.set(op)

# Medidas de los botones
ancho = 8
alto = 3
# Declarar variable
sali = StringVar()

# FONDO
ventana.config(background='#F5A9F2')
# Creamos los botones
btnSqr = tk.Button(ventana, text="sqrt", width=ancho, height=alto, font=('arial',10), bg='#BE81F7', command=lambda:entrada('sqrt')).place(x= 30, y=120)
btnCe = tk.Button(ventana, text="CE", width=ancho, height=alto, font=('arial',10), bg='#BE81F7', command=limpiar).place(x= 110,y=120)
btnC = tk.Button(ventana, text="C", width=ancho, height=alto, font=('arial',10), bg='#BE81F7', command=borrarUno).place(x= 190, y=120)
btnDiv = tk.Button(ventana, text="/", width=ancho, height=alto, font=('arial',10), bg='#BE81F7', command=lambda:entrada('/')).place(x= 270, y=120)
btn7 = tk.Button(ventana, text="7", width=ancho, height=alto, font=('arial',10), bg='#F781F3', command=lambda:entrada('7')).place(x= 30, y=185)
btn8 = tk.Button(ventana, text="8", width=ancho, height=alto, font=('arial',10), bg='#F781F3', command=lambda:entrada('8')).place(x= 110, y=185)
btn9 = tk.Button(ventana, text="9", width=ancho, height=alto, font=('arial',10), bg='#F781F3', command=lambda:entrada('9')).place(x= 190, y=185)
btnRe = tk.Button(ventana, text="-", width=ancho, height=alto, font=('arial',10), bg='#BE81F7', command=lambda:entrada('-')).place(x= 270, y=185)
btn4 = tk.Button(ventana, text="4", width=ancho, height=alto, font=('arial',10), bg='#F781F3', command=lambda:entrada('4')).place(x= 30, y=250)
btn5 = tk.Button(ventana, text="5", width=ancho, height=alto, font=('arial',10), bg='#F781F3', command=lambda:entrada('5')).place(x= 110, y=250)
btn6 = tk.Button(ventana, text="6", width=ancho, height=alto, font=('arial',10), bg='#F781F3', command=lambda:entrada('6')).place(x= 190, y=250)
btnSum = tk.Button(ventana, text="+", width=ancho, height=alto, font=('arial',10), bg='#BE81F7', command=lambda:entrada('+')).place(x= 270, y=250)
btn1 = tk.Button(ventana, text="1", width=ancho, height=alto, font=('arial',10), bg='#F781F3', command=lambda:entrada('1')).place(x= 30, y=315)
btn2 = tk.Button(ventana, text="2", width=ancho, height=alto, font=('arial',10), bg='#F781F3', command=lambda:entrada('2')).place(x= 110, y=315)
btn3 = tk.Button(ventana, text="3", width=ancho, height=alto, font=('arial',10), bg='#F781F3', command=lambda:entrada('3')).place(x= 190, y=315)
btnMulti = tk.Button(ventana, text="x", width=ancho, height=alto, font=('arial',10), bg='#BE81F7', command=lambda:entrada('*')).place(x= 270, y=315)
btn0 = tk.Button(ventana, text="0", width=18, height=alto, font=('arial',10), bg='#F781F3', command=lambda:entrada('0')).place(x= 30, y=380)
btnP = tk.Button(ventana, text=".", width=ancho, height=alto, font=('arial',10), bg='#F781F3', command=lambda:entrada('.')).place(x= 190, y=380)
btnIgual = tk.Button(ventana, text="=", width=ancho, height=alto, font=('arial',10), bg='#BE81F7', command= resultado).place(x= 270, y=380)


# input de salida
salida = tk.Entry(ventana, width=17, textvariable=sali, state= "disabled") 
salida.config(font=('arial',25),  borderwidth=5)
salida.place(x=30, y=40)
ventana.mainloop()  