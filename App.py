import customtkinter
from tkinter import *
import Soma
import Subtrair
import Multiplicar
import Dividir

customtkinter.set_appearance_mode("light")
window = customtkinter.CTk()
window.geometry("640x360")
window.title("App")
window.resizable(False, False)
label = customtkinter.CTkLabel(window, text="Calculadora")
label.place(x=288, y=92)
button1 = customtkinter.CTkButton(window, width=137, height=25, text="Somar", command=Soma.abrir)
button1.place(x=252, y=126)
button2 = customtkinter.CTkButton(window, width=137, height=25, text="Subtrair", command=Subtrair.abrir)
button2.place(x=252, y=165)
button3 = customtkinter.CTkButton(window, width=137, height=25, text="Multiplicar", command=Multiplicar.abrir)
button3.place(x=252, y=204)
button4 = customtkinter.CTkButton(window, width=137, height=25, text="Dividir", command=Dividir.abrir)
button4.place(x=252, y=243)

window.mainloop()