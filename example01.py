from xengine import * 
from OpenGL.GL import * # pip install PyOpenGL
from math import sqrt

def setup():
    a = 1
    h = a * sqrt(3) / 2

    A = Point(-a/2, -h/2,   0, RED)
    B = Point(a/2,  -h/2,   0, GREEN)
    C = Point(0,    h/2,    0, BLUE)

    V = Triangle(A, B, C)
    V.draw()

def loop():
    glDrawArrays(GL_TRIANGLES, 0, 3)

window = Window(720, 480, "XEngine Window", SETUP_FUNCTION=setup, LOOP_FUNCTION=loop)
