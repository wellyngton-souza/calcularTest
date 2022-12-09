import customtkinter
from tkinter import *

def abrir():
    window = customtkinter.CTk()
    window.geometry("640x360")
    window.title("Subtrair")
    window.resizable(False, False)

    customtkinter.set_default_color_theme("green")

    global label, textbox1, textbox2

    label = customtkinter.CTkLabel(window, text="Subtrair")
    label.place(x=301, y=116)
    textbox1 = customtkinter.CTkEntry(window, width=137, height=25)
    textbox1.place(x=251, y=150)
    textbox2 = customtkinter.CTkEntry(window, width=137, height=25)
    textbox2.place(x=251, y=189)

    def Subtrair():
        resultado = int(textbox1.get()) - int(textbox2.get())
        label.configure(text="Resultado: " + str(resultado))

    button = customtkinter.CTkButton(window, width=137, height=25, text="Calcular", command=Subtrair)
    button.place(x=251, y=228)

    window.mainloop()