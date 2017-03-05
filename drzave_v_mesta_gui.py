# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import Tkinter
import random
import tkMessageBox


def klik_gumba():
    odg = guess.get()
    if odg == "Ljubljana":
        tkMessageBox.showinfo("Vaš odgovor", "Odgovor je pravilen!")
    else:
        tkMessageBox.showerror("Vaš odgovor", "Odgovor je napačen")

def klik_gumba1():
    odg1 = guess1.get()
    if odg1 == "Dunaj":
        tkMessageBox.showinfo("Vaš odgovor", "Odgovor je pravilen!")
    else:
        tkMessageBox.showerror("Vaš odgovor", "Odgovor je napačen")


def klik_gumba2():
    odg2 = guess2.get()
    if odg2 == "Rim":
        tkMessageBox.showinfo("Vaš odgovor", "Odgovor je pravilen!")
    else:
        tkMessageBox.showerror("Vaš odgovor", "Odgovor je napačen")


window = Tkinter.Tk()
window.title("Ugani glavno mesto države")
window.geometry("400x400")
window.configure(bg="medium spring green")


vpr = Tkinter.Label(window, bg="medium spring green", text="Katero je glavno mesto Slovenije?")
vpr.config(font=("garamond", 15))
vpr.pack()


guess = Tkinter.Entry(window)
guess.config(fg="darkgreen")
guess.pack(padx=10, pady=15)

button = Tkinter.Button(text="Preveri", command=klik_gumba, width=8, bg="gray")
button.pack()


vpr = Tkinter.Label(window, bg="medium spring green", text="Katero je glavno mesto Avstrije?")
vpr.config(font=("garamond", 15))
vpr.pack()


guess1 = Tkinter.Entry(window)
guess1.config(fg="darkgreen")
guess1.pack(padx=10, pady=15)

button = Tkinter.Button(text="Preveri", command=klik_gumba1, width=8, bg="gray")
button.pack()


vpr = Tkinter.Label(window, bg="medium spring green", text="Katero je glavno mesto Italije?")
vpr.config(font=("garamond", 15))
vpr.pack()


guess2 = Tkinter.Entry(window)
guess2.config(fg="darkgreen")
guess2.pack(padx=10, pady=15)

button = Tkinter.Button(text="Preveri", command=klik_gumba2, width=8, bg="gray")
button.pack()

window.mainloop()