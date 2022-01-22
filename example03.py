from xengine import *
from OpenGL.GL import * # pip install PyOpenGL

from xengine.shaders import STANDARD_SHADER

vertex_shader, fragment_shader = STANDARD_SHADER

def setup(window):
    a = 300
    
    A = Point(0,    0,  0, MAGENTA)
    B = Point(a,    0,  0, CIAN)
    C = Point(0,    a,  0, YELLOW)
    D = Point(a,    a,  0, MAGENTA)
    
    T = GeneralShape(A, B, C, D)
    T.adapt_to_window(window)
    T.set_shader(vertex_shader, fragment_shader)
    T.draw()

def loop(window):
    glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

window = Window(720, 580, setup_function=setup, loop_function=loop)
