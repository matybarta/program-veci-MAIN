import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox



#věci na okno
window = tk.Tk()
window.geometry("1280x720")
window.title("Komunikace do neznáma")
window.config(background="Black")

#tlačítka
exit_button = tk.Button(window, text="Konec komunikace", font=("Comic sans MS", 14), fg="White", background="Dark red", command=exit)
exit_button.place(x=1110, y=680)

#komunikace hehe

odpoved = "Ahoj"

otazka = tk.StringVar()

otazka_form = tk.Entry(window,font=("Comic sans MS",14), textvariable=otazka)
otazka_form.place(x=515, y=300)

label = tk.Label(text="Ahahaha", background="Black", font=("Comic sans MS", 10,), fg="Green", width=150, height=10)
label.place(x=40, y=350)

def press(otazka):
    vec = otazka.get()
    if vec == "Ahoj":
        label.config(text="hola")

zprava_button = tk.Button(window,text="Odeslat zprávu", font=("Comic sans MS", 14), fg="White", background="#040924", command=press(otazka))
zprava_button.place(x=565, y= 250)


window.mainloop()