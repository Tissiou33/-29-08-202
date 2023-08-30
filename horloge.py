
import tkinter as tk
import time

fenetre = tk.Tk()
fenetre.title("Horloge GMT")
fenetre.geometry("300x300")
fenetre.resizable(False, False)
#fenetre.bg = "black"

label = tk.Label(fenetre, font=("Arial", 40), bg="black", fg="white")
label.place(x=50, y=130)

#fonction de mise a jour de l'heure
def mise_a_jour():
    heure = time.strftime("%H:%M:%S", time.gmtime())
    label.config(text=heure)
    fenetre.after(1000, mise_a_jour)

mise_a_jour()
fenetre.mainloop()