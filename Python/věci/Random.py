import tkinter as tk

#věci na okno
window = tk.Tk()
window.geometry("1280x720")
window.title("Hádací hra")
window.config(background="Light green")

#Něco random na test
label = tk.Label(text="Tohle je hádací hra. Pokud chcete začít klikněte na start.", background="Sea green", font=("Comic sans MS", 10,), width=200, height=2)
label.pack()


#tlačítka
exit_button = tk.Button(window, text="Konec", font=("Comic sans MS", 14), fg="White", background="Blue", command=exit)
exit_button.place(x=1211, y=680)

start_button = tk.Button(window, text="Start", font=("Comic sans MS", 14), fg="White", background="Blue")
start_button.place(x=0, y=680)

guess_button = tk.Button(window,text="Hádat", font=("Comic sans MS", 14), fg="White", background="Blue")
guess_button.place(x=600, y= 300)

#hra
guessed_number = tk.StringVar()

number_form = tk.Entry(window,font=("Comic sans MS",14), textvariable=guessed_number)
number_form.place(x=515, y=350)




window.mainloop()