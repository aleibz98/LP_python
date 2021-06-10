from vpython import *
import math


class Turtle3D:
    # Atributs de la classe

    # Operacions públiques

    # PINTAR
    def forward(self, distance):
        # calculem punt final
        incX = distance * math.cos(self.angleTilt) * math.cos(self.angleUp)
        incY = distance * math.sin(self.angleTilt) * math.cos(self.angleUp)
        incZ = distance * math.sin(self.angleUp)

        x, y, z = self.pos
        self.pos = (incX, incY, incZ)

        # pintem el cilindre si es necessari
        if self.painting:
            cylinder(pos=vector(x, y, z), axis=vector(incX, incY, incZ), radius=self.radio, color=self.color)

        # Fem update dels atributs de la classe
        self.pos = (x + incX, y + incY, z + incZ)

    def backward(self, distance):
        # calculem punt final
        incX = distance * math.cos(self.angleTilt) * math.cos(self.angleUp)
        incY = distance * math.sin(self.angleTilt) * math.cos(self.angleUp)
        incZ = distance * math.sin(self.angleUp)

        x, y, z = self.pos
        self.pos = (incX, incY, incZ)

        # pintem el cilindre si es necessari
        if self.painting:
            cylinder(pos=vector(x, y, z), axis=vector(-incX, -incY, -incZ), radius=self.radio, color=self.color)

        # Fem update dels atributs de la classe
        self.pos = (x - incX, y - incY, z - incZ)

    # ROTAR
    def left(self, angle):
        self.angleTilt -= math.radians(angle)

    def right(self, angle):
        self.angleTilt += math.radians(angle)
        print(self.angleTilt)

    def up(self, angle):
        self.angleUp += math.radians(angle)

    def down(self, angle):
        self.angleUp -= math.radians(angle)

    def hide(self):
        self.painting = False

    def show(self):
        self.painting = True

    def home(self):
        self.pos = (0, 0, 0)

    def cambiaColor(self, x,y,z):
        self.color = vector(x,y,z)

    def cambiaRadio(self, r):
        self.radio = r

    # Operacions privades
    def __init__(self):
        scene.height = scene.width = 1000
        scene.autocenter = True
        scene.caption = "Hello World"

        self.angleUp = 0
        self.angleTilt = 0
        self.pos = (0, 0, 0)
        self.painting = True
        self.radio = 0.1
        self.color = color.red


#turtle = Turtle3D()

"""
#TEST 1
for i in range(4):
    turtle.forward(10)
    turtle.right(90)
"""
"""
#TEST 2
def cercle(mida,costats):
    for i in range(1,costats):
        turtle.forward(mida)
        turtle.left(360 / costats)

def espiral(cercles):
    if cercles > 0:
        cercle(1,12)
        turtle.up(5)
        espiral(cercles-1)

espiral(5)
"""