import tkinter as tk

class Entidad:
    def __init__(self):
        self.posx = 0
        self.posy = 0
    def getPosicion(self):
        return [self.posx,self.posy]
    def setPosicion(self,npx,npy):
        self.posx = npx
        self.posy = npy

class Nave(Entidad):
    def __init__(self):
        super().__init__()

class Jugador(Nave):
    def __init__(self):
        super().__init__()
        
def mueveJugador1(direccion):
    global jugador1
    x,y = Jug1.getPosicion()
    if direccion == "arriba":
        y -= 1
    elif direccion == "abajo":
        y += 1
    elif direccion == "izquierda":
        x -= 1
    elif direccion == "derecha":
        x += 1
    Jug1.setPosicion(x,y)
    lienzo.coords(jugador1,x,y)

def mueveJugador2(direccion):
    global jugador2
    x,y = Jug2.getPosicion()
    if direccion == "arriba":
        y -= 1
    elif direccion == "abajo":
        y += 1
    elif direccion == "izquierda":
        x -= 1
    elif direccion == "derecha":
        x += 1
    Jug2.setPosicion(x,y)
    lienzo.coords(jugador2,x,y)
    
raiz = tk.Tk()
raiz.title("Alien Invaders")
raiz.geometry("512x512")

lienzo = tk.Canvas(raiz,width=512,height=512)
lienzo.pack()

Jug1 = Jugador()
Jug2 = Jugador()

jugador1img = tk.PhotoImage(file="nave1.png")
jugador1imgescalado = jugador1img.zoom(2)
jugador1 = lienzo.create_image(20,20,image=jugador1imgescalado)

jugador2img = tk.PhotoImage(file="nave2.png")
jugador2imgescalado = jugador2img.zoom(2)
jugador2 = lienzo.create_image(50,20,image=jugador2imgescalado)

raiz.bind("<w>",lambda event:mueveJugador1("arriba"))
raiz.bind("<s>",lambda event:mueveJugador1("abajo"))
raiz.bind("<a>",lambda event:mueveJugador1("izquierda"))
raiz.bind("<d>",lambda event:mueveJugador1("derecha"))

raiz.bind("<Up>",lambda event:mueveJugador2("arriba"))
raiz.bind("<Down>",lambda event:mueveJugador2("abajo"))
raiz.bind("<Left>",lambda event:mueveJugador2("izquierda"))
raiz.bind("<Right>",lambda event:mueveJugador2("derecha"))

raiz.mainloop()
