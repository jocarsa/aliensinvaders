import tkinter as tk

raiz = tk.Tk()
raiz.title("Alien Invaders")
raiz.geometry("512x512")

lienzo = tk.Canvas(raiz,width=512,height=512)
lienzo.pack()

jugador1img = tk.PhotoImage(file="nave1.png")
jugador1imgescalado = jugador1img.zoom(2)
jugador1 = lienzo.create_image(20,20,image=jugador1imgescalado)

jugador2img = tk.PhotoImage(file="nave2.png")
jugador2imgescalado = jugador2img.zoom(2)
jugador2 = lienzo.create_image(50,20,image=jugador2imgescalado)

raiz.mainloop()
