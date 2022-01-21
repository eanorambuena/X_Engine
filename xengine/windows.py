import  glfw # pip install glfw
from    OpenGL.GL import (
    glClear,
    glClearColor,
    GL_COLOR_BUFFER_BIT,
) # pip install PyOpenGL

from xengine.types import   UNDEFINED, NONE

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

        self.internal_vars = {}

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

        self.setup_function(self)

        if window is UNDEFINED:
            raise Exception("UNDEFINED_ERROR: Window not created in setup function while auto_setup is set to False")

        return window

    def loop(self):
        t = 0
        while not glfw.window_should_close(self.GL_WINDOW) and t < self.limit_time:
            glfw.poll_events() # Verify events are correct

            glClear(GL_COLOR_BUFFER_BIT)

            self.loop_function(self) # Drawing code
            
            glfw.swap_buffers(self.GL_WINDOW) # Swap the Drawing buffer with the Display buffer

            t += 1

        glfw.terminate() # Close
