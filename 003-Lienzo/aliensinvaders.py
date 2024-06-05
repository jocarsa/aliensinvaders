import tkinter as tk

raiz = tk.Tk()
raiz.title("Alien Invaders")
raiz.geometry("512x512")

lienzo = tk.Canvas(raiz,width=512,height=512)
lienzo.pack()

raiz.mainloop()
