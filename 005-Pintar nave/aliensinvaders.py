import tkinter as tk

raiz = tk.Tk()
raiz.title("Alien Invaders")
raiz.geometry("512x512")

lienzo = tk.Canvas(raiz,width=512,height=512)
lienzo.pack()

jugador1img = tk.PhotoImage(file="nave1.png")
jugador1 = lienzo.create_image(20,20,image=jugador1img)

raiz.mainloop()
