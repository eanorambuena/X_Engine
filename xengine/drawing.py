import  glfw # pip install glfw
import  numpy as np
from    OpenGL.GL import (
    glClear,
    glClearColor,
    glColorPointer,
    glEnableClientState,
    glVertexPointer,
    GL_COLOR_ARRAY,
    GL_COLOR_BUFFER_BIT,
    GL_FLOAT,
    GL_VERTEX_ARRAY
) # pip install PyOpenGL

from xengine.colors import  *
from xengine.types import   UNDEFINED

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

    def __init__(self, width = 720, heigth = 480, title = "XEngine Window", monitor = None, share = None, FPS = 60, setup_function = NONE, loop_function = NONE, auto_setup = True, limit_time = 10 ** 5):
        self.width = width
        self.height = heigth
        self.title = title
        self.monitor = monitor
        self.share = share
        self.limit_time = limit_time
        self.FPS = FPS
        self.setup_function = setup_function
        self.loop_function = loop_function
        self.auto_setup = auto_setup

        self.GL_WINDOW = self.setup()
        self.loop()

    def setup(self):

        window = UNDEFINED

        if self.auto_setup:
            if not glfw.init(): # Initialize the window
                return

            window = glfw.create_window(self.width, self.height, self.title, self.monitor, self.share)

            if not window:
                glfw.terminate()
                return
            
            glfw.make_context_current(window) # Make the window the current window

            glClearColor(1, 1, 1, 1)

        self.setup_function()

        if window is UNDEFINED:
            raise Exception("UNDEFINED_ERROR: Window not created in setup function while auto_setup is set to False")

        return window

    def loop(self):
        t = 0
        while not glfw.window_should_close(self.GL_WINDOW) and t < self.limit_time:
            glfw.poll_events() # Verify events are correct

            glClear(GL_COLOR_BUFFER_BIT)

            self.loop_function() # Drawing code
            
            glfw.swap_buffers(self.GL_WINDOW) # Swap the Drawing buffer with the Display buffer

            t += 1

        glfw.terminate() # Close
