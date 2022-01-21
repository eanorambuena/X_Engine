import numpy as np

from xengine.colors import  *
from xengine.types import   UNDEFINED

class Point(list):

    def __init__(self, x = 0, y = 0, z = 0, RGBA = WHITE):
        super().__init__([x, y, z, RGBA])

        self.vertices = np.array([x, y, z], dtype=np.float32)

        self.color = np.array([RGBA[0], RGBA[1], RGBA[2], RGBA[3]], dtype=np.float32)

    def adapt_to_window(self, window = UNDEFINED, width = UNDEFINED, height = UNDEFINED):

        if window is not UNDEFINED:
            mid_width = window.width / 2
            mid_height = window.height / 2

        else:
            mid_width = width / 2
            mid_height = height / 2

        self.vertices = np.array([self.x / mid_width, self.y / mid_height, self.z], dtype=np.float32)

    @property
    def x(self):
        return self.vertices[0]
    
    @property
    def y(self):
        return self.vertices[1]
    
    @property
    def z(self):
        return self.vertices[2]

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
