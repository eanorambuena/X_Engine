import glfw      # pip install glfw
from OpenGL.GL import * # pip install PyOpenGL
import numpy as np

from xengine.colors import *

class Point(list):

    def __init__(self, x = 0, y = 0, z = 0, RGBA = WHITE):
        super().__init__([x, y, z, RGBA])

        self.verteces = np.array([x, y, z], dtype=np.float32)

        self.color = np.array([RGBA[0], RGBA[1], RGBA[2], RGBA[3]], dtype=np.float32)

    @property
    def x(self):
        return self.verteces[0]
    
    @property
    def y(self):
        return self.verteces[1]
    
    @property
    def z(self):
        return self.verteces[2]

    @property
    def R(self):
        return self.color[0]

    @property
    def G(self):
        return self.color[1]
    
    @property
    def B(self):
        return self.color[2]

    @property
    def A(self):
        return self.color[3]

class Triangle(list):

    def __init__(self, point_1, point_2, point_3):
        super().__init__([point_1, point_2, point_3])

        self.verteces = np.array([  point_1.x, point_1.y, point_1.z,
                                    point_2.x, point_2.y, point_2.z,
                                    point_3.x, point_3.y, point_3.z],
                                    dtype=np.float32)

        self.colors = np.array([point_1.R, point_1.G, point_1.B, point_1.A,
                                point_2.R, point_2.G, point_2.B, point_2.A,
                                point_3.R, point_3.G, point_3.B, point_3.A],
                                dtype=np.float32)

    def draw(self):
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, self.verteces)

        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(4, GL_FLOAT, 0, self.colors)

def NONE():
    return

class Window:

    def __init__(self, WIDTH = 720, HEIGHT = 480, TITLE = "XEngine Window", MONITOR = None, SHARE = None, LIMIT_TIME = 10 ** 5, FPS = 60, SETUP_FUNCTION = NONE, LOOP_FUNCTION = NONE):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TITLE = TITLE
        self.MONITOR = MONITOR
        self.SHARE = SHARE
        self.LIMIT_TIME = LIMIT_TIME
        self.FPS = FPS
        self.SETUP_FUNCTION = SETUP_FUNCTION
        self.LOOP_FUNCTION = LOOP_FUNCTION

        self.GL_WINDOW = self.setup()
        self.loop()

    def setup(self):

        if not glfw.init(): # Initialize the window
            return

        window = glfw.create_window(self.WIDTH, self.HEIGHT, self.TITLE, self.MONITOR, self.SHARE)

        if not window:
            glfw.terminate()
            return
        
        glfw.make_context_current(window) # Make the window the current window

        glClearColor(1, 1, 1, 1)

        self.SETUP_FUNCTION()

        return window

    def loop(self):
        t = 0
        while not glfw.window_should_close(self.GL_WINDOW) and t < self.LIMIT_TIME:
            glfw.poll_events() # Verify events are correct

            glClear(GL_COLOR_BUFFER_BIT)

            self.LOOP_FUNCTION() # Drawing code
            
            glfw.swap_buffers(self.GL_WINDOW) # Swap the Drawing buffer with the Display buffer

            t += 1

        glfw.terminate() # Close
