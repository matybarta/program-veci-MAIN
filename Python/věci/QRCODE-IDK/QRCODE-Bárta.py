"""
Pro správné fungování nainstalujte tyto knihovny: pyqrcode, pypng.
Nainstalujete je tím, že do terminálu dáte: pip3 install pyqrcode/pypng
"""
import tkinter as tk
import pyqrcode as qr



#basic věci na okno
okno = tk.Tk()
okno.geometry("1280x800")
okno.title("Nevim")

#Místo na zapsání webovky
psani = tk.Entry(okno, font=("Comic sans MS", 20), background="Blue", foreground="White")
psani.place(x = 50, y = 200)

#Místo kde se ukáže QR kód
zobrazeni = tk.Label(okno, text="Zde se ukáže QR kód", borderwidth = 2, relief="solid")
zobrazeni.place(x = 500, y = 50)


#funkce na vytvoření QR kódu
def generace_qr():
    global my_img
    qr_obraz = qr.create(psani.get()) 
    qr_obraz.png('qr_kod.png', scale = 6, 
        module_color = [0, 0, 0, 0], background = [255,255,255,255]) 
    qr_obraz = qr_obraz.xbm(scale = 10)
    my_img = tk.BitmapImage(data = qr_obraz)
    zobrazeni.config(image = my_img)

#tlačítko na vygenerování QR kódu
tlacidlo = tk.Button(okno, font=("Comic sans MS", 20), background="Blue", foreground="White", text="Generovat QR kód", command=lambda:generace_qr())
tlacidlo.place(x = 85, y = 300)

okno.mainloop()
