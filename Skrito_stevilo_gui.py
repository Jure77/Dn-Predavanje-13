# -*- coding: utf-8 -*-

import Tkinter
import random
import tkMessageBox

secret = random.randint(1, 20)

def klik_gumba():
    if int(guess.get()) == secret:
        rezultat = "Pravilno"
    elif int(guess.get()) > secret:
        rezultat = "Tvoje število je previsoko."
    elif int(guess.get()) < secret:
        rezultat = "Tvoje število je prenizko."
    else:
        rezultat = "Napačno"

    tkMessageBox.showinfo("Rezultat", rezultat)

window = Tkinter.Tk()
window.title("Skrito število")
window.geometry("400x400")
window.configure(bg="deep sky blue")


vpr = Tkinter.Label(window, bg="deep sky blue", text="Ugani skrito število med 1 in 20")
vpr.config(font=("perpetua", 15))
vpr.pack()


guess = Tkinter.Entry(window)
guess.config(fg="darkgreen")
guess.pack(padx=10, pady=15)

button = Tkinter.Button(text="Preveri", command=klik_gumba, width=8, bg="gray")
button.pack()



window.mainloop()