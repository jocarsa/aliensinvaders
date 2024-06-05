import tkinter as tk
import random

class Entidad:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.velocidad = 5
    def getPosicion(self):
        return [self.posx,self.posy]
    def setPosicion(self,npx,npy):
        self.posx = npx
        self.posy = npy
    def getVelocidad(self):
        return self.velocidad

class Nave(Entidad):
    def __init__(self):
        super().__init__()
        
class Jugador(Nave):
    def __init__(self):
        super().__init__()

class Estrella(Entidad):
    def __init__(self):
        super().__init__()
        
        
def mueveJugador1(direccion):
    global jugador1
    x,y = Jug1.getPosicion()
    if direccion == "arriba" and y > 0:
        y -= Jug1.getVelocidad()
    elif direccion == "abajo" and y < 512:
        y += Jug1.getVelocidad()
    elif direccion == "izquierda" and x > 0:
        x -= Jug1.getVelocidad()
    elif direccion == "derecha" and x < 512:
        x += Jug1.getVelocidad()
    Jug1.setPosicion(x,y)
    lienzo.coords(jugador1,x,y)

def mueveJugador2(direccion):
    global jugador2
    x,y = Jug2.getPosicion()
    if direccion == "arriba" and y > 0:
        y -= Jug2.getVelocidad()
    elif direccion == "abajo" and y < 512:
        y += Jug2.getVelocidad()
    elif direccion == "izquierda" and x > 0:
        x -= Jug2.getVelocidad()
    elif direccion == "derecha" and x < 512:
        x += Jug2.getVelocidad()
    Jug2.setPosicion(x,y)
    lienzo.coords(jugador2,x,y)

def nuevaBalaJugador1():
    print(jugador1img)
    x,y = lienzo.coords(jugador1)
    balas.append(lienzo.create_rectangle(x,y,x-2,y-10,fill="white"))

def nuevaBalaJugador2():
    print(jugador1img)
    x,y = lienzo.coords(jugador2)
    balas.append(lienzo.create_rectangle(x,y,x-2,y-10,fill="white"))
    
raiz = tk.Tk()
raiz.title("Alien Invaders")
raiz.geometry("512x512")

lienzo = tk.Canvas(raiz,width=512,height=512)
lienzo.pack()
lienzo.create_rectangle(0,0,512,512,fill="black")

estrellas = []
numeroestrellas = 100
formaestrellas = []

for i in range(0,numeroestrellas):
    x = random.randint(0,512)
    y = random.randint(0,512)
    estrellas.append(Estrella())
    estrellas[-1].setPosicion(x,y)
    formaestrellas.append(lienzo.create_rectangle(x,y,x+2,y+2,fill="white"))

balas = []


Jug1 = Jugador()
Jug1.setPosicion(128,450)
Jug2 = Jugador()
Jug2.setPosicion(384,450)



jugador1img = tk.PhotoImage(file="nave1.png")
jugador1imgescalado = jugador1img.zoom(2)
jugador1 = lienzo.create_image(128,450,image=jugador1imgescalado)

jugador2img = tk.PhotoImage(file="nave2.png")
jugador2imgescalado = jugador2img.zoom(2)
jugador2 = lienzo.create_image(384,450,image=jugador2imgescalado)

raiz.bind("<w>",lambda event:mueveJugador1("arriba"))
raiz.bind("<s>",lambda event:mueveJugador1("abajo"))
raiz.bind("<a>",lambda event:mueveJugador1("izquierda"))
raiz.bind("<d>",lambda event:mueveJugador1("derecha"))

raiz.bind("<space>",lambda event:nuevaBalaJugador1())

raiz.bind("<Up>",lambda event:mueveJugador2("arriba"))
raiz.bind("<Down>",lambda event:mueveJugador2("abajo"))
raiz.bind("<Left>",lambda event:mueveJugador2("izquierda"))
raiz.bind("<Right>",lambda event:mueveJugador2("derecha"))

raiz.bind("<KeyPress-minus>",lambda event:nuevaBalaJugador2())


def bucle():
    for estrella in formaestrellas:
        lienzo.move(estrella,0,5)
        if lienzo.coords(estrella)[1] > 512:
            lienzo.move(estrella,0,-512)
    for bala in balas:
        lienzo.move(bala,0,-5)
       
    raiz.after(100,bucle)

bucle()

raiz.mainloop()










