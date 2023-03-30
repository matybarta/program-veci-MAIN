import tkinter as tk

okno = tk.Tk()
okno.geometry("1280x800")
okno.title("Nevim")

psani = tk.Entry(okno, font=("Comic sans MS", 20), background="Blue", foreground="White")
psani.place(x = 50, y = 200)

#Místo kde se ukáže QR kód
zobrazeni = tk.Label(okno, text="Zde se ukáže QR kód", borderwidth = 2, relief="solid")
zobrazeni.place(x = 500, y = 50)