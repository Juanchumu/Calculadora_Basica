#Calculadora Simple v0.01
from tkinter import *

root = Tk()

#Definir un titulo para la ventana de la aplicacion
root.title("Calculadora Simple")

#Definir una entrada de datos


e = Entry(root, width=35, bg="gray", fg="white", borderwidth=5)
e.grid(row= 1, column=0, columnspan=3,padx=10, pady=10)
#e.get()
#e.insert(0, "")



def boton_click(numero):
    
    #e.delete(0, END) #Borrar lo que esta en la casilla
    current = e.get()
    e.delete(0, END)
    
    e.insert(0, str(current) + str(numero)) #insertar lo que aprete recien

#funciones de operadores

def calc_boton_mas():
    primer_numero = e.get()
    global p_numero
    global calculo
    calculo = "Suma"
    p_numero = int(primer_numero)
    e.delete(0, END)
    
    
def calc_boton_menos():
    primer_numero = e.get()
    global p_numero
    global calculo
    calculo = "Resta"
    p_numero = int(primer_numero)
    e.delete(0, END)
    
def calc_boton_por():
    primer_numero = e.get()
    global p_numero
    global calculo
    calculo = "Multiplicacion"
    p_numero = int(primer_numero)
    e.delete(0, END)
    
def calc_boton_dividido():
    primer_numero = e.get()
    global p_numero
    global calculo
    calculo = "Division"
    p_numero = int(primer_numero)
    e.delete(0, END)
    

def calc_boton_limpiar():
    e.delete(0, END)  
    
    
def calc_boton_igual():
    segundo_numero = e.get()
    e.delete(0, END)
    if calculo == "Suma":
        e.insert(0, p_numero + int(segundo_numero))
    if calculo == "Resta":
        e.insert(0, p_numero - int(segundo_numero))
    if calculo == "Multiplicacion":
        e.insert(0, p_numero * int(segundo_numero))
    if calculo == "Division":
        e.insert(0, p_numero / int(segundo_numero))
    
#Funcion Sobre mi

def sobremi():
    top =  Toplevel()
    top.title("Sobre Mi!")
    top.geometry("400x200")
    
    frame_en_top = LabelFrame(top, text="Calculadora Simple", padx=15, pady= 15)
    texto_dentro_del_frame = Label(frame_en_top, text="holaaaa es lo primero que subi a github", padx=15, pady=15)
    texto_dentro_del_frame_1 = Label(frame_en_top, text="Hello!! im Juanchumu!", padx=15)
    boton_2 = Button(top, text="Cerrar ventana)", command=top.destroy)
    
    #Gridear despues
    frame_en_top.grid(row=0 , column=0, padx=15, pady=15, columnspan= 1)
    texto_dentro_del_frame.grid(row=0, column= 0)
    texto_dentro_del_frame_1.grid(row=1 ,column=0)
    boton_2.grid(row=1 , column=0)
    

#definir cada boton de la calculadora con su accion

boton_1 = Button(root, text="1",padx=40,pady=20,command=lambda: boton_click(1))
boton_2 = Button(root, text="2",padx=40,pady=20,command=lambda: boton_click(2))
boton_3 = Button(root, text="3",padx=40,pady=20,command=lambda: boton_click(3))
boton_4 = Button(root, text="4",padx=40,pady=20,command=lambda: boton_click(4))
boton_5 = Button(root, text="5",padx=40,pady=20,command=lambda: boton_click(5))
boton_6 = Button(root, text="6",padx=40,pady=20,command=lambda: boton_click(6))
boton_7 = Button(root, text="7",padx=40,pady=20,command=lambda: boton_click(7))
boton_8 = Button(root, text="8",padx=40,pady=20,command=lambda: boton_click(8))
boton_9 = Button(root, text="9",padx=40,pady=20,command=lambda: boton_click(9))
boton_0 = Button(root, text="0",padx=40,pady=20,command=lambda: boton_click(0))
 
boton_mas      = Button(root, text="+",padx=40,pady=20,command=calc_boton_mas)
boton_menos    = Button(root, text="-",padx=40,pady=20,command=calc_boton_menos)
boton_por      = Button(root, text="*",padx=40,pady=20,command=calc_boton_por)
boton_dividido = Button(root, text="/",padx=40,pady=20,command=calc_boton_dividido)

boton_igual = Button(root, text="=",padx=180,pady=20,command=calc_boton_igual) 

boton_limpiar = Button(root, text="Limpiar",padx=70,pady=20,command=calc_boton_limpiar) #no necesita lambda




#Para dejarlo mas lindo se packea/gridea despues
# poner los botones en la pantalla

boton_1.grid(row=4 , column=0)
boton_2.grid(row=4 , column=1)
boton_3.grid(row=4 , column=2)

boton_4.grid(row=3 , column=0)
boton_5.grid(row=3 , column=1)
boton_6.grid(row=3 , column=2)

boton_7.grid(row=2 , column=0)
boton_8.grid(row=2 , column=1)
boton_9.grid(row=2 , column=2)

boton_0.grid(row=5 , column=0)

boton_mas.grid(     row=4 , column=3)
boton_menos.grid(   row=4 , column=4)
boton_por.grid(     row=3 , column=3)
boton_dividido.grid(row=3 , column=4)

boton_igual.grid(row=5 , column=1,   columnspan= 4)
boton_limpiar.grid(row=2 , column=3, columnspan = 2)

#boton sobre mi

sobre_mi = Button(root, text="Sobre Mi", command=sobremi)
sobre_mi.grid(row=0, column=4)




root.mainloop()
